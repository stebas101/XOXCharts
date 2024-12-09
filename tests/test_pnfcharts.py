import os

basedir = os.path.abspath(os.path.dirname(__file__))

def data_file(symbol: str) -> str:
    return os.path.join(basedir, 'data') + symbol.upper() + '.csv'

def test_load_data():
    pass