from enum import Enum, unique


@unique
class TableColumns(Enum):
    """Enum used to describe type of column in table of simulation"""
    CLIENT_ID = 0
    TEC = 1

    START_SW_GO = 2
    DURATION_SW_GO = 3
    END_SW_GO = 4

    START_SA_GO = 5
    DURATION_SA_GO = 6
    END_SA_GO = 7

    START_DB = 8
    DURATION_DB = 9
    END_DB = 10

    START_SA_RETURN = 11
    DURATION_SA_RETURN = 12
    END_SA_RETURN = 13

    START_SW_RETURN = 14
    DURATION_SW_RETURN = 15
    END_SW_RETURN = 16

    ANSWER = 17
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

    def populate_initial_simulation_data(self, tec):
        for idx, client in enumerate(self.table):
            client[0] = idx
            client[1] = self.table[idx - 1][1] + tec if idx > 0 else tec


# table = SimulationTable(clients_number=4)
# table.populate_initial_simulation_data(tec=0.01)
# print(table.table)
