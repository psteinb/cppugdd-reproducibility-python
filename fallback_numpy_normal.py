import numpy as np
import math

def test_generate():

    np.random.seed(42)
    res = np.random.normal(5,2,10)
    exp = [5.99342831, 4.7234714 , 6.29537708, 8.04605971, 4.53169325,
           4.53172609, 8.15842563, 6.53486946, 4.06105123, 6.08512009]

    for i in range(len(res)):
        assert math.fabs(res[i] == exp[i]) < 1e-7

if __name__ == '__main__':
    test_generate()
