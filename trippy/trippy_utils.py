import numpy as num


def extent(r1, r2, n):
    """
    :param r1:
    :param r2:
    :param n:
    :return:
    """
    lr1 = num.log10(r1)
    lr2 = num.log10(r2)

    return 10.0 ** (num.linspace(lr1, lr2, n))


def expand2d(a, repFact):
    """
    Rebin a 2d array to a large size.
    output will be xrepfact, xrepfact of the original
    Basic memory enhancements included to speed things up.
    :param a:
    :param repFact:
    :return:
    """
    (A, B) = a.shape
    if A * repFact < 1000 and B * repFact < 1000:
        return num.repeat(num.repeat(a, repFact, axis=0), repFact, axis=1) / (repFact * repFact)
    else:
        out = num.zeros((A * repFact, B * repFact), dtype=a.dtype)
        for i in range(A):
            r = num.repeat(a[i], repFact)
            for j in range(repFact):
                out[i * repFact + j, :] = r
        return out / (float(repFact) * float(repFact))

def downSample2d(a, sampFact):
    """

    :param a:
    :param sampFact:
    :return: a downsampled numpy.ndarray
    """
    (A, B) = a.shape
    A /= sampFact
    B /= sampFact
    return num.array([num.sum(a[i:i + sampFact, j:j + sampFact]) for i in range(0, sampFact * A, sampFact) for j in
                      range(0, sampFact * B, sampFact)]).reshape(A, B) / (sampFact * sampFact)


class line:
    """

    """
    def __init__(self, p1, p2):
        self.m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        self.b = p2[1] - self.m * p2[0]
        self.xlim = num.array([min(p1[0], p2[0]), max(p1[0], p2[0])])
        self.ylim = num.array([min(p1[1], p2[1]), max(p1[1], p2[1])])

    def __call__(self, x):
        return self.m * x + self.b
