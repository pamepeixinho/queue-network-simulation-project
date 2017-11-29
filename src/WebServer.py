"""
    Web server, also known as SW in the problem description

    Function: Calculate processing time of messages in this server (BY INTERACTION)

    Problem Desc: "Os tempos de processamento no servidor de Web também dependem do
    tipo de processo. Deve durar algo entre 4 mseg. e 6 mseg. (uniformemente distribuídos)
    no processamento referente ao nó dois da interação tipo 1. Deve durar algo entre 5 mseg.
    e 7 mseg. no processamento do nó dois e entre 7 mseg. e 10 mseg. no processamento
    referente ao nó cinco da mesma interação. Finalmente, para a interação tipo 3 os tempos
    nos nós 2 e 9 ficam entre 9 mseg. e 12 mseg."
"""

from src.UniformDistribution import uniform_distribution
from src.InteractionType import InteractionType


class WebServer:

    @staticmethod
    def get_processing_time(interaction_type):
        """
            Get Processing time (Duration)
        :param interaction_type: InteractionType
        :return: tuple (duration_ws_in and duration_ws_out)
        """
        if interaction_type == InteractionType.INTERACTION_ONE:
            return uniform_distribution(4, 6), 0
        elif interaction_type == InteractionType.INTERACTION_TWO:
            return uniform_distribution(5, 7), uniform_distribution(7, 10)
        return 0
