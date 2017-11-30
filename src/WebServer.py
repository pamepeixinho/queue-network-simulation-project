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
                table[idx][TableColumns.START_WS_IN] = (client.m1.size / velocity) + client_arrival_instant
            else:
                table[idx][TableColumns.START_WS_IN] = client.m1.size / velocity + max(
                    table[idx][TableColumns.ARRIVAL_INSTANT],
                    table[idx - 1][TableColumns.END_WS_IN])

            table[idx][TableColumns.DURATION_WS_IN] = duration
            table[idx][TableColumns.END_WS_IN] = table[idx][TableColumns.START_WS_IN] + duration
            table[idx][TableColumns.INTERACTION.value] = client.interaction.value
        return table

    @staticmethod
    def simulate_server_out(table, clients, velocity):
        aux_table = table.copy()
        first_back, aux_table = WebServer.get_minimum_as_out(table=aux_table, clients=clients)
        while first_back:
            fb_index = first_back['index']
            table[fb_index][TableColumns.START_WS_OUT] = (clients[fb_index].m8.size / velocity) + table[fb_index][
                first_back['column']]
            duration = clients[fb_index].wsOutDuration
            table[fb_index][TableColumns.DURATION_WS_OUT] = duration
            table[fb_index][TableColumns.END_WS_OUT] = table[fb_index][first_back['column']] + duration
            first_back, aux_table = WebServer.get_minimum_as_out(table=aux_table, clients=clients)
        return table

    @staticmethod
    def get_minimum_as_out(table, clients):
        returning_from_db = []
        returning_from_as = []

        for idx, client in enumerate(clients):
            if client.interaction == InteractionType.INTERACTION_TWO:
                # get all values of END_AS
                returning_from_as.append({
                    'index': idx,
                    'time': table[idx][TableColumns.END_AS_IN],
                    'column': TableColumns.END_AS_IN.value,
                })

            if client.interaction == InteractionType.INTERACTION_THREE:
                # get all values of END_AS
                returning_from_db.append({
                    'index': idx,
                    'time': table[idx][TableColumns.END_DB],
                    'column': TableColumns.END_DB.value,
                })

        if len(returning_from_db) == 0 or len(returning_from_db) == 0:
            return None, table

        min_db_by_time = min(returning_from_db, key=lambda c: c['time'])  # min by time
        min_as_by_time = min(returning_from_db, key=lambda c: c['time'])  # min by time

        if min_db_by_time['time'] == 999999 and min_as_by_time['time'] == 999999:
            return None, table
        elif min_db_by_time['time'] < min_as_by_time['time']:
            table[min_db_by_time['index']][min_db_by_time['column']] = 999999
            return min_db_by_time, table
        else:
            table[min_as_by_time['index']][min_as_by_time['column']] = 999999
            return min_as_by_time, table
