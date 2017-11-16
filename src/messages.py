import random


class Message:
    """ Represents messages"""
    def __init__(self, index):
        self.index = index

    @staticmethod
    def get_message_weight(p1, p2, p3):
        return random.triangular(p1, p2, p3)