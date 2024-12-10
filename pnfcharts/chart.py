import pandas as pd

class chart():
    """Use this class to create chart objects based on time series data, either price only, or 'high, low, close'
    """
    SCALE_TYPES = ('linear', 'log', 'custom')
    PRICE_TYPES = ('close', 'hlc', 'c')
    
    _scale: tuple[float] # the y-axis values
    _data: pd.DataFrame
    _chart = dict()
    _scale_type: str # linear, log or 'standard'
    _price_type: str # close or hlc
    _box_size: float
    _reversal: int
    name: str
    
    def __init__(self, name: str,
                 scale_type: str, price_type: str,
                 box_size: float, reversal: int,
                 csv_file: str) -> None:
        """Steps to init a chart object:
        
        - load data into a dataframe
        - generate scale
        - initialize chart (gets first X or O)

        Args:
            name (str): a name for the chart
        """
        self.name = name
        
        if scale_type in self.SCALE_TYPES:
            self._scale_type = scale_type
        else:
            raise "InvalidScaleType"
        if price_type in self.PRICE_TYPES:
            self._price_type = price_type
        else:
            raise "InvalidPriceType"
        
        # TODO validate data file
        self._load_data(csv_file)
                  
        self._box_size = box_size
        self._reversal = reversal
    
    def _load_data(self, csv_file: str):
        df = pd.read_csv(csv_file)
        headings = [c.lower() for c in df.columns] # convert column names to lowercase
        df.columns = headings
        assert 'date' in headings
        df.index = pd.to_datetime(df['date'])
        assert 'close' in headings or 'price' in headings # this allows for columns named 'Adj Close' or 'Price'

        if self._price_type == 'close':
            # select the first column that contains either 'close' or 'price'
            sel_col = [h for h in headings if ('close' in h) or ('price' in h)][0]
            self._data = df[sel_col].copy()
        elif self._price_type == 'hlc':
            assert 'high' in headings and 'low' in headings
            self._data =df[['high', 'low', 'close']]
            
    def head(self, n: int = 5) -> pd.DataFrame:
        """Returns the first n rows of the chart data as a pandas DataFrame or Series

        Args:
            n (int): number of data rows

        Returns:
            pd.DataFrame: the head of the chart data
        """
        return self._data.head(n)
        
    def tail(self, n: int = 5) -> pd.DataFrame:
        """Returns the last n rows of the chart data as a pandas DataFrame or Series

        Args:
            n (int): number of data rows

        Returns:
            pd.DataFrame: the head of the chart data
        """
        return self._data.tail(n)
        
    def set_scale() -> None:
        pass
    
    def get_scale():
        pass
    
    def _init_chart() -> None:
        pass
    
    def __repr__(self):
        return f"PNF Chart for {self.name}\n{self._box_size = }, {self._reversal = }"