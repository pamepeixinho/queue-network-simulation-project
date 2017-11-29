from Client import Client
from SimulationTable import SimulationTable
from constants import velocity, arrival_instant


def simulation(clients_number):
    """
        Simulation of queue network
    """
    clients = [Client() for x in range(clients_number)]

    table = SimulationTable(clients_number=clients_number)
    table.populate_initial_simulation_data(arrival_instant=arrival_instant)

    print(clients)
    print(table)



simulation(clients_number=30)
