import os

from pnfcharts import chart

basedir = os.path.abspath(os.path.dirname(__file__))

def data_file(symbol: str) -> str:
    return os.path.join(basedir, 'data', symbol.upper() + '.csv')

def test_chart():
    file = data_file('EXP1')
    chart1 = chart('Test', scale_type='linear', price_type='close', box_size=1, reversal=3, csv_file=file)
    assert "PNF Chart for Test" in str(chart1)
    # assert : chart data as DataFrame or Series?
    
    file2 = data_file('EXP2')
    chart2 = chart('Test', scale_type='linear', price_type='hlc', box_size=1, reversal=3, csv_file=file2)
    for col in ('high', 'low', 'close'):
        assert col in chart2.head().columns
