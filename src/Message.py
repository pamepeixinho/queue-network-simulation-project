import random


class Message:
    """ Represents messages"""

    def __init__(self, p1, p2, p3):
        self.size = self.triangular_distribution(p1, p2, p3) * 1.1

    @classmethod
    def triangular_distribution(cls, p1, p2, p3):
        """Make triangular distribution ("Distribuicao Triangular")"""
        return random.triangular(p1, p2, p3)
