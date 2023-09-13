import xox_pnf.pnfplot as pnf
import numpy as np
import pytest


@pytest.mark.parametrize("test_parameters,expected",
                         [((10, 100, 10, 'linear'), np.arange(0,120,10)),
                          ((36.50, 40.25, 1, 'linear'), np.arange(36,42,1)),
                          ((36.50, 40.25, 2, 'linear'), np.arange(36, 43, 2)),
                          ])
def test_generate_scale(test_parameters, expected):
    low, high, box_size, method = test_parameters
    scale = pnf.generate_scale (low, high, box_size, method)
    assert np.array_equal(scale, expected)



