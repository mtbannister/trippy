__author__ = 'bannisterm'

import pytest

@pytest.mark.parametrize(('values', 'result'),
                          [([1], 1),
                           ([1,2], 3),
                           ([1,2,3], 6)
                           ])
def test_sum(values, result):
    assert sum(values) == result


# Data files need to be in the directory where the tests are being run

def test_write(tmpdir):
    filename = tmpdir.join('data.txt').strpath
    with open(filename, 'w') as f:
        f.write("Banana!")