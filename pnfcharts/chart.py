import pandas as pd

class chart():
    """_summary_
    """
    SCALE_TYPES = ('linear')
    PRICE_TYPES = ('close', 'hlc')
    
    scale: tuple[float] # the y-axis values
    scale_type: str # linear, log or 'standard'
    price_type: str # close or hlc
    data: pd.DataFrame
    
    def __init__(self, symbol: str, scale_type: str, price_type: str) -> None:
        """_summary_
        
        - load data into a dataframe
        - generate scale

        Args:
            symbol (str): _description_
        """
        if scale_type in self.SCALE_TYPES:
            self.scale_type = scale_type
        else:
            raise "InvalidScaleType"
        if price_type in self.PRICE_TYPES:
            self.price_type = price_type
        else:
            raise "InvalidPriceType"
        
        # call load data
    
    def load_data():
        pass
    
    def set_scale() -> None:
        pass
    
    def get_scale():
        pass
    
    