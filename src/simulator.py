# Simulate 250 clients in the system
from src.SimulationTable import SimulationTable


def simulation(clients_number):
    velocity = 80000000
    tec = 0.0005

    #  TODO: create msgs

    table = SimulationTable(clients_number=clients_number)
    table.populate_initial_simulation_data(tec=tec)
