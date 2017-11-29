from enum import Enum, unique


@unique
class TableColumns(Enum):
    """Enum used to describe type of column in table of simulation"""
    CLIENT_ID = 0
    ARRIVAL_INSTANT = 1

    START_WS_IN = 2
    DURATION_WS_IN = 3
    END_WS_IN = 4

    START_AS_IN = 5
    DURATION_AS_IN = 6
    END_AS_IN = 7

    START_DB = 8
    DURATION_DB = 9
    END_DB = 10

    START_AS_OUT = 11
    DURATION_AS_OUT = 12
    END_AS_OUT = 13

    START_WS_OUT = 14
    DURATION_WS_OUT = 15
    END_WS_OUT = 16

    ANWSER = 17
    INTERACTION = 18


def column_header_name():
    return ['ClienteID',
            'Instante de chegada',
            'Inicio SW (ida)',
            'Duracao SW (ida)',
            'Fim SW (ida)',
            'Inicio SA (ida)',
            'Duracao SA (ida)',
            'Fim SA (ida)',
            'Inicio DB',
            'Duracao DB',
            'Fim DB',
            'Inicio SA (volta)',
            'Duracao SA (volta)',
            'Fim SA (volta)',
            'Inicio SW (volta)',
            'Duracao SW (volta)',
            'Fim SW (volta)',
            'Recepcao da resposta',
            'Interacao',
            ]


class SimulationTable:
    """Structure of the simulation table used in queue network """

    def __init__(self, clients_number=250):
        """
            Creates a table with columns from (column_header_name size)
            by clients number with 250 as default
        """
        self.clients_number = clients_number
        self.table = [[0.0 for x in range(len(column_header_name()))] for y in range(clients_number)]

    def populate_initial_simulation_data(self, arrival_instant):
        for idx, client in enumerate(self.table):
            client[0] = idx
            client[1] = self.table[idx - 1][1] + arrival_instant if idx > 0 else arrival_instant


# table = SimulationTable(clients_number=4)
# table.populate_initial_simulation_data(arrival_instant=0.01)
# print(table.table)
