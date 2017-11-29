import numpy.random as random


def triangular_distribution(p1, p2, p3):
    """Make triangular distribution ("Distribuicao Triangular")"""
    return random.triangular(p1, p2, p3)


class Message:
    """ Represents messages"""

    def __init__(self, p1, p2, p3):
        self.size = triangular_distribution(p1, p2, p3) * 1.1
