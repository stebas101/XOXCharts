import pandas as pd
import numpy as np


def generate_column_range(scale, range_low, range_high):
    '''
    Takes in the high and low extremes of a box range and returns the whole
    range as a np.array representing a set of boxes

    Args:
        scale: np.array
        range_low: int or float
        range_high: into or float

    Returns:
        col_range: np.array
    '''
    col_range = scale[np.logical_and(scale >= range_low, scale <= range_high)]
    
    return col_range 


def init_pnf(scale,
             high,
             low,
             close,
             reversal_size,
             box_range=[]):
    '''
    returns trend status as num value (either 0, 1 or -1) and box_range as np.array
    
    Args:
        scale: np.array - the scale for the chart
        high: float - high price
        low: float  - low price
        close: float - closing/last price
        reversal_size: int > 0
        box_range: np.array or empty list
        
    Returns:
        status: int (-1,0, or 1)
        box_range: np.array
    '''
    # TODO: fix zero-size array error:
    if len(box_range) == 0:
        box_range = scale[np.logical_and(scale>=low, scale<=high)]
    else:
        box_range = scale[np.logical_and(scale>=min(box_range.min(), low), scale<=max(box_range.max(), high))]
#         box_range = generate_column_range()
        
    mid_price = 0.5 * box_range.min() + 0.5 * box_range.max()

    if len(box_range) >= reversal_size and close > mid_price:
        status = 1
    elif len(box_range) >= reversal_size and close < mid_price:
        status = -1
    else:
        status = 0
        
    return status, box_range


def update_pnf(scale,
               high,
               low,
               status,
               reversal_size,
               box_low,
               box_high):
    '''
    updates the chart once the trend status is defined
    returns status and box_range for the day
    
    Args:
        scale:
        high:
        low:
        status:
        reversal_size:
        box_low:
        box_high:
    Returns:
        status: int (-1,0, or 1)
        box_range: np.array
    '''
#     box_range = scale[np.logical_and(scale>=box_low, scale<=box_high)] # needed in case we return the current range
    box_range = generate_column_range(scale, box_low, box_high)
    box_reverse = []
    # new temporary box range with extensions on both sides:
#     box_range_new = scale[np.logical_and(scale>=min(low, box_low), scale<=max(high, box_high))]
    box_range_new = generate_column_range(scale, min(low, box_low), max(high, box_high))
    box_high_new = box_range_new.max()
    box_low_new = box_range_new.min()
    
    if status == 1:
        # check for upper extensions, else for reversals
        if box_high_new > box_high:
            box_range = scale[np.logical_and(scale>=box_low, scale<=box_high_new)]
#             use generate_...()
        # check for potential reversal
        elif low < box_high:
            box_reverse = scale[np.logical_and(scale>=low, scale<=box_high)][:-1]    
#             use generate_...()
                  
    if status == -1:
        if box_low_new < box_low:
            box_range = scale[np.logical_and(scale>=box_low_new, scale<=box_high)]
        elif high > box_low:
            box_reverse = scale[np.logical_and(scale>=box_low, scale<=high)][1:]

    # Check potential reversal against reversal_size and reverse status if needed:      
    if len(box_reverse) >= reversal_size:
        status *= -1 # reverse trend status
        box_range = box_reverse # update box_range

    return status, box_range


def get_pnf_ranges(price_data, scale, reversal_size):

    # initialise status and box arrays:
    trend_status = np.zeros(len(price_data))
    box_low = np.zeros(len(price_data))
    box_high = np.zeros(len(price_data))

    # Initialise the chart until a trend status (+/-1) is found
    box_range = []
    for index, row in enumerate(price_data.iterrows()):
        high = row[1]['High']
        low = row[1]['Low']
        close = row[1]['Close']
        status, box_range = init_pnf(scale, high, low, close, reversal_size, box_range)
        trend_status[index] = status
        box_low[index] = box_range.min()
        box_high[index] = box_range.max()
        if status != 0:
            break

    # TODO:
    # Check if there are more lines of data to process
    # print(index + 1 < len(price_data))
    # return column if not true

    # Next, we need to process the remaining lines of price:
    start = index + 1
    for index, row in enumerate(price_data.iloc[start:].iterrows()):
        high = row[1]['High']
        low = row[1]['Low']
        status = trend_status[index + start - 1]
        box_l = box_low[index + start - 1]
        box_h = box_high[index + start - 1]
        status, box_range = update_pnf(scale,
                                       high,
                                       low,
                                       status,
                                       reversal_size,
                                       box_l,
                                       box_h)
        trend_status[index+start] = status
        box_low[index+start] = box_range.min()
        box_high[index+start] = box_range.max()

    pnf_data = pd.DataFrame({'trend_status': trend_status,
                             'range_low': box_low,
                             'range_high': box_high
                            })

    return pnf_data


def get_pnf_changes(pnf_data):
    '''
    Args: pd.DataFrame - w/ trend_status, range_low, range_high

    Returns: pd.DataFrame - with changes column
    '''
    trend_status = pnf_data['trend_status']
    changes = (np.diff(np.sign(trend_status)) != 0)
    # We make sure that the a column is generated for the last price line:
    changes = np.append(changes, [True])
    # Note that the change column is 'shifted': it's True when a status change is detected on the next price line:
    pnf_data['change'] = changes

    return pnf_data


def get_pnf_columns(pnf_data, scale):
    ranges = []
    trends = []

    # should we use .apply() here?
    for row in pnf_data[pnf_data['change']].iterrows():
        row = row[1]
        col_range = generate_column_range(scale,
                                          row['range_low'], row['range_high'])
        ranges.append(col_range)
        trends.append(row['trend_status'])

    columns = list(zip(trends, ranges))

    return columns


def get_price_data(data_file):
    '''
    Args:
    - String - a csv file name

    - Returns: pd.DataFrame with High, Low, Close
    - TO DO: return df with Close/Last only
    '''
    # TODO: allow to process data with Close/Last only
    # TODO: handle exceptions when file is not found
    data = pd.read_csv('xox_pnf/data/' + data_file, index_col="Date")
    data.index = pd.to_datetime(data.index) # Converting the dates from string to datetime format
    price_data = data[['High','Low','Close']]

    return price_data


def pnf_text(scale, columns):
    '''
    Generates a text PnF chart
    
    Args:
        scale: np.array
        columns: list of tuples (int, np.array)
    Returns:
        grid: a list of strings (representing chart lines)
    '''
    hpad = 2 # padding columns on the sides
    marker = {0:'*', 1:'X', -1:'O'}
    grid = []

    for line_price in np.flip(scale):
        line = f"{line_price}|{'.' * hpad}"
        for col in columns:
            line += marker[col[0]] if line_price in col[1] else '.'
        line += f"{'.' * hpad}|{line_price}"
        grid.append(line)
    
    # return grid[:-1] # removing the last newline
    return grid

# TODO the above functions should be moved within the PnfChart class

class PnfChart():
    
    def __init__(self, chart_params):
        data_file = chart_params['data_file']
        self.symbol = data_file[:-4]
        
        self.reversal_size = chart_params['reversal_size']
        self.box_size = chart_params['box_size']
        self.method = 'linear'
        self._price_data = get_price_data(data_file)
        self.first_day = self._price_data.index[0]
        self.last_day = self._price_data.index[-1]
        
        low = self._price_data['Low'].min()
        high = self._price_data['High'].max()
        params = (low, high, self.box_size, self.method)
        self.scale = self._get_scale(params)
        
        pnf_data = get_pnf_ranges(self._price_data, self.scale, self.reversal_size)
        self.pnf_data = get_pnf_changes(pnf_data)
        
        self.columns = get_pnf_columns(pnf_data, self.scale)        
        self.text = pnf_text(self.scale, self.columns)
        
    def __str__(self):
        return '\n'.join(self.text)
    
    def __repr__(self):
        return f'PnF chart of {self.symbol}'

    def _get_scale(self, params):
        '''
        Args:
        - params: tuple:
            - low:  float or int
            - high: float or int
            - box_size: positive float or int
            - method: string in ['linear', 'log', 'variable']

        Returns:
        - scale: np.array
        '''
        # TODO:
        # - log method

        low, high, box_size, method = params

        # table for variable box size
        # (from, to, box_size)
        # TODO: the chart must accept custom tables
        box_size_table = [(0, 6, 0.1),
                        (6, 14, 0.2),
                        (14, 29, 0.5),
                        (29, 60, 1),
                        (60, 140, 2),
                        (140, 290, 5),
                        (290, 600, 10),
                        (600, 1400, 20)
                        ]

        def round_ends(low, high, box_size):
            start = (low // box_size) *  box_size
            end  = (high // box_size) * box_size + box_size
            start = (start - box_size) if low % box_size == 0 else start   
            return start, end    

        # TODO: refactor using match/case - requires Python 3.10
        if method == 'linear': 
            start, end = round_ends(low, high, box_size)
            scale = np.arange(start=start, stop=end+box_size, step=box_size)
        elif method == 'variable':
            # round ends
            for row in box_size_table:
                a, b, box_size = row
                if low >= a and low < b:
                    break
            start, _ = round_ends(low, high, box_size)
            start -= box_size
            for row in box_size_table:
                a, b, box_size = row
                if high >= a and high < b:
                    break
            _, end = round_ends(low, high, box_size)
            end += box_size

            # generate scale
            scale = np.array([])
            for row in box_size_table:
                a, b, box_size = row
                if a <= end and b >= start:
                    arr = np.arange(max(a, start), min(b, end), box_size)
                    scale = np.concatenate((scale, arr))
        elif method == 'log':
            pass
                    
        return scale
