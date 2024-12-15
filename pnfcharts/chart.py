import pandas as pd
import numpy as np


class PnfChart():
    """Use this class to create chart objects based on time series data
    This is the price only version, for 'high, low, close' another class will inherit ans override
    
    Attributes:
    _data: pd.DataFrame or pd.Series
    _box_size: float
    _fixed_scale: tuple(float) # to be used as an alternative to box_size
    _reversal: int
    _scale_type: str # linear, log or 'standard'
    _scale: tuple[float] # the y-axis values
    _price_type: str # close or hlc
    name: str
    price_interval: str in ['daily', 'weekly', 'monthly']
    first_date
    last_date
    length (num of columns)
    _chart = dict() # the actual data needed to plot the pnf chart
    
    """
    SCALE_TYPES = ('linear', 'log', 'fixed')
    PRICE_INTERVALS = ('daily', 'weekly', 'monthly')
    
    
    def __init__(self, name: str,
                 scale_type: str,
                 reversal: int,
                 data: pd.Series,
                 box_size: float = None,
                 fixed_scale: tuple[float] = None,
                 ) -> None:
        """Steps to init a chart object:
        
        - load data into a dataframe
        - generate scale
        - initialize chart (gets first X or O)
        - update chart iteratively

        Args:
            name (str): a name for the chart
        """
        self.name = name
        
        if scale_type in self.SCALE_TYPES:
            self._scale_type = scale_type
        else:
            raise "InvalidScaleType"
        # if price_type in self.PRICE_TYPES:
        #     self._price_type = price_type
        # else:
        #     raise "InvalidPriceType"
        
        self._data = data
        
        if box_size and box_size > 0:
            self._box_size = box_size
        elif fixed_scale:
            # TODO
            pass
        else:
            raise "A valid box_size or fixed_scale id needed."
        if isinstance(reversal, int) and reversal > 0:
            self._reversal = reversal
        else:
            raise "'reversal' needs to be a positive integer."
    

    @property
    def box_size(self):
        if self._box_size:
            return self._box_size
        
    @property
    def reversal(self):
        return self._reversal
    
    @property
    def scale_type(self):
        return self._scale_type
    
    def head(self, n: int = 5) -> pd.Series:
        """Returns the first n rows of the chart data as a pandas DataFrame or Series

        Args:
            n (int): number of data rows

        Returns:
            pd.Series: the head of the chart data
        """
        return self._data.head(n)
        
    def tail(self, n: int = 5) -> pd.Series:
        """Returns the last n rows of the chart data as a pandas DataFrame or Series

        Args:
            n (int): number of data rows

        Returns:
            pd.Series: the head of the chart data
        """
        return self._data.tail(n)

        
    @property
    def scale(self):
        return self._scale
    
    @scale.setter
    def scale() -> None:
        pass
    
    def _init_chart() -> None:
        pass
    
    
    def __repr__(self):
        return f"PNF Chart for {self.name}\n{self._box_size = }, {self._reversal = }"


class Scale():
    def __init__(self, data: object):
        self._data = data
        self._scale = np.array([])
        
    @property
    def type(self):
        return self._type
    
    @property
    def scale(self):
        return self._scale
    
    @property
    def length(self):
        return len(self._scale)


class LinearScale(Scale):
    def __init__(self, data, box_size: float):
        super().__init__(data)
        self._type = 'linear'
        self._box_size = box_size
        self.set_scale()
        
    @property
    def box_size(self):
        return self._box_size

    def set_scale(self):
        max_price = self._data.max()
        min_price = self._data.min()
        start, end = round_ends(min_price, max_price, self.box_size)
        scale = np.arange(start=start, stop=end+self.box_size, step=self.box_size)
        self._scale = scale


class LogScale(Scale):
    pass


class FixedScale(Scale):
    pass


def chart(name: str,
          scale_type: str,
          reversal: int,
          csv_file: str,
          box_size: float = None,
          fixed_scale: tuple[float] = None,):
    
    data = load_csv_series(csv_file)
    
    return PnfChart(name,
                    scale_type,
                    reversal,
                    data,
                    box_size = None,
                    fixed_scale = None,
                 )

def load_csv_series(csv_file: str) -> pd.Series:
    """This function reads a csv file to get the price time series.
    A valid file must include a 'date' column and a 'price' or 'close' column (the names are case insensitive).
    If more than one column that includes the word 'close' or 'price' is included, the first one is selected.

    Args:
        csv_file (str): a valid file path

    Returns:
        pd.Series: the price time series
    """
    df = pd.read_csv(csv_file)
    headings = [c.lower() for c in df.columns] # convert column names to lowercase
    df.columns = headings
    assert 'date' in headings
    assert 'close' in headings or 'price' in headings # this allows for columns named 'Adj Close' or 'Price'
    df.index = pd.to_datetime(df['date'])

    # select the first column that contains either 'close' or 'price'
    sel_col = [h for h in headings if ('close' in h) or ('price' in h)][0]
    data = df[sel_col].copy()
    return data

def round_ends(low: float, high: float, box_size: float) -> tuple[float, float]:
    """_summary_

    Args:
        low (float): _description_
        high (float): _description_
        box_size (float): _description_

    Returns:
        tuple[float, float]: _description_
    """
    start = (low // box_size) *  box_size
    end  = (high // box_size) * box_size + box_size
    start = (start - box_size) if low % box_size == 0 else start   
    return start, end  