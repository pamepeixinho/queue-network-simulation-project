"""
    Database server, also known as DB in the problem description

    Function: Calculate processing time of messages in this server

    Problem Desc: "O tempo de processamento no servidor de banco de dados (nó sete da interação tipo 3)
     se divide em duas parcelas, ambas uniformemente distribuídas. Entre 15 mseg e 30 mseg
     de processamento e entre 50 mseg e 400 mseg de acesso a disco."
"""
from UniformDistribution import uniform_distribution

from InteractionType import InteractionType
from SimulationTable import TableColumns


class DatabaseServer:
    @staticmethod
    def get_processing_time():
        """
            Get Processing time (Duration)
        :return: tuple (duration_ws_in and duration_ws_out)
        """
        return uniform_distribution(15, 30) + uniform_distribution(50, 400)

    @staticmethod
    def simulate_server(table, clients, velocity):
        first = True
        last_index = None
        tablet = ''
        for idx, client in enumerate(clients):
            duration = client.bdDuration
            if client.interaction == InteractionType.INTERACTION_THREE:
                if first:
                    table[idx][TableColumns.START_DB] = (client.m6.size / velocity) + table[idx][
                        TableColumns.END_AS_IN]
                    first = False
                else:
                    table[idx][TableColumns.START_AS_IN] = (client.m3.size / velocity) + max(
                        table[idx][TableColumns.END_AS_IN],
                        table[last_index][TableColumns.END_DB])

            last_index = idx
            table[idx][TableColumns.DURATION_DB] = duration
            table[idx][TableColumns.END_DB] = table[idx][TableColumns.START_DB] + duration
            return table
