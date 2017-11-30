"""
    Application server, also known as SA in the problem description

    Function: Calculate processing time of messages in this server (by last node visited)

    Problem Desc: "Os tempos de processamento no servidor de aplicações dependerão
    do tipo de processo. Deve durar algo entre 40 mseg. e 60 mseg. (uniformemente
    distribuídos) no processamento referente ao nó quatro. Já para o processamento
    referente ao nó oito, os tempos mínimo e máximo são 60 mseg. e 120 mseg.,
    respectivamente."
"""

from UniformDistribution import uniform_distribution
from SimulationTable import TableColumns

from InteractionType import InteractionType


class ApplicationServer:
    @staticmethod
    def get_processing_time():
        """
            Get Processing time (Duration)
        :return: tuple (duration_ws_in and duration_ws_out)
        """
        return uniform_distribution(40, 60), uniform_distribution(60, 120)

    @staticmethod
    def simulate_server_in(table, clients, velocity):
        first = True
        last_index = None
        tablet = ''
        for idx, client in enumerate(clients):
            duration = client.asInDuration
            if client.interaction != InteractionType.INTERACTION_ONE.value:
                if first:
                    table[idx][TableColumns.START_AS_IN] = (client.m3.size / velocity) + table[idx][
                        TableColumns.END_WS_IN]
                    first = False
                else:
                    table[idx][TableColumns.START_AS_IN] = (client.m3.size / velocity) + max(
                        table[idx][TableColumns.END_WS_IN],
                        table[last_index][TableColumns.END_AS_IN])
            last_index = idx

            table[idx][TableColumns.DURATION_AS_IN] = duration
            table[idx][TableColumns.END_AS_IN] = table[idx][TableColumns.START_AS_IN] + duration
            return table

    @staticmethod
    def simulate_server_out(table, clients, velocity):
        aux_table = table.copy()
        first_back, aux_table = ApplicationServer.get_minimum_as_out(table=aux_table, clients=clients)
        while first_back:
            fb_index = first_back['index']
            table[fb_index][TableColumns.START_AS_OUT] = (clients[fb_index].m7.size / velocity) + table[fb_index][
                first_back['column']]
            duration = clients[fb_index].asOutDuration
            table[fb_index][TableColumns.DURATION_AS_OUT] = duration
            table[fb_index][TableColumns.END_AS_OUT] = table[fb_index][first_back['column']] + duration
            first_back, aux_table = ApplicationServer.get_minimum_as_out(table=aux_table, clients=clients)
        return table

    @staticmethod
    def get_minimum_as_out(table, clients):
        returning_from_db = []

        for idx, client in enumerate(clients):
            if client.interaction == InteractionType.INTERACTION_THREE:
                # get all values of END_DB
                returning_from_db.append({
                    'index': idx,
                    'time': table[idx][TableColumns.END_DB],
                    'column': TableColumns.END_DB.value,
                })

        min_client_by_time = min(returning_from_db, key=lambda c: c['time'])  # min by time
        if min_client_by_time['time'] == 999999:
            return None, table

        table[min_client_by_time['index']][min_client_by_time['column']] = 999999
        return min_client_by_time, table
