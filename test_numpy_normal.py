import numpy as np
import pytest

def test_generate():

    np.random.seed(42)
    res = np.random.normal(6,2,10)
    exp = [6.99342831, 5.7234714 , 7.29537708, 9.04605971, 5.53169325,
           5.53172609, 9.15842563, 7.53486946, 5.06105123, 7.08512009]

    for i in range(len(res)):
        assert res[i] == pytest.approx(exp[i])
