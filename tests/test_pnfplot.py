import xox_pnf.pnfplot as pnf
import numpy as np
import pytest

exp1 = {
    'data_file': 'EXP1.csv',
    'reversal_size': 3,
    'box_size': 1,
    'plot_method': 'high-low',
    'scale_method': 'linear',
}

@pytest.mark.parametrize("test_parameters,expected",
                         [((10, 100, 10, 'linear'), np.arange(0, 120, 10)),
                          ((36.50, 40.25, 1, 'linear'), np.arange(36, 42, 1)),
                          ((36.50, 40.25, 2, 'linear'), np.arange(36, 43, 2)),
                          ((14, 21.5, 0.5, 'linear'), np.arange(13.5, 22.5, 0.5)),
                          ((6.32, 20.89, 1, 'variable'), np.concatenate((np.arange(6, 14, 0.2), 
                                                                         np.arange(14, 21.5, 0.5)))),
                          ])
def test_get_scale(test_parameters, expected):
    # low, high, box_size, method = test_parameters
    pnf_chart = pnf.PnfChart(exp1)
    scale = pnf_chart._get_scale (test_parameters)
    assert np.array_equal(scale, expected)



