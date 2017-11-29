# Simulate 250 clients in the system

from src.SimulationTable import SimulationTable
from src.constants import velocity, tec


def simulation(clients_number):
    #  TODO: create msgs

    table = SimulationTable(clients_number=clients_number)
    table.populate_initial_simulation_data(tec=tec)
