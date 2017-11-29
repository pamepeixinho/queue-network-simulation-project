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

from UniformDistribution import uniform_distribution
from InteractionType import InteractionType
from SimulationTable import TableColumns

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
        else:
            return uniform_distribution(9, 12), uniform_distribution(9, 12)

    @staticmethod
    def simulate_server_in(table, clients, velocity):
        for idx, client in enumerate(clients):
            client_arrival_instant = table[idx][TableColumns.ARRIVAL_INSTANT]
            duration = client.wsInDuration

            if idx == 0:
                table[idx][TableColumns.START_WS_IN] = (client.m1 / velocity) + client_arrival_instant
                table[idx][TableColumns.DURATION_WS_IN] = duration
                table[idx][TableColumns.END_WS_IN] = table[idx][TableColumns.START_WS_IN] + duration
            else:
                # Max(arrival_instant, end_ws)
                return 1