import os

import pandas as pd
import numpy as np

from pnfcharts import PnfChart, load_csv_series, LinearScale, Scale

basedir = os.path.abspath(os.path.dirname(__file__))

def data_file(symbol: str) -> str:
    return os.path.join(basedir, 'data', symbol.upper() + '.csv')

# def test_chart():
#     file = data_file('EXP1')
#     chart1 = PnfChart('Test', scale_type='linear', reversal=3, csv_file=file, box_size=1,)
#     assert "PNF Chart for Test" in str(chart1)
#     # assert : chart data as DataFrame or Series?
#     assert chart1.scale_type == 'linear'
#     assert chart1.box_size == 1
#     assert chart1.reversal == 3
    
    # test invalid scale
    # test invalid box size
    # test invalid reversal
    # test invalid file
    
    # file2 = data_file('EXP2')
    # chart2 = PnfChart('Test', scale_type='linear', price_type='hlc', box_size=1, reversal=3, csv_file=file2)
    # for col in ('high', 'low', 'close'):
    #     assert col in chart2.head().columns

def test_scale():
    # testing load_csv_series
    file = data_file('EXP1')
    data = load_csv_series(file)
    assert isinstance(data, pd.Series)
    
    # testing the parent Scale class
    scale2 = Scale(data)
    assert scale2.scale.size == 0
    
    # testing LinearScale
    scale = LinearScale(data, box_size = 1)
    assert scale.type == 'linear'
    assert scale.length == 4
    
    # testing round_ends
    
