import sys
import csv

from Client import Client
from WebServer import WebServer
from ApplicationServer import ApplicationServer
from DatabaseServer import DatabaseServer
from SimulationTable import SimulationTable, TableColumns, column_header_name
from constants import velocity, arrival_instant


def calculate_final(table, clients):
    for idx, client in clients:
        final_index = 16
        if client.interaction == InteractionType.INTERACTION_ONE:
            final_index = 4
        table[idx][TableColumns.ANSWER] = table[idx][final_index] + (client.m2.size / velocity) + client.requestDuration
    return table


def save_simulation_csv(table):
    f = open('simulation_result.csv', 'w')
    writer = csv.writer(f, delimiter=',', quotechar='"', lineterminator='\n')
    writer.writerow(list(column_header_name()))
    for row in table:
        writer.writerow(row)
    f.close()


def simulation(clients_number):
    """
        Simulation of queue network
    """
    clients = [Client() for x in range(clients_number)]

    simulation_table = SimulationTable(clients_number=clients_number)
    simulation_table.populate_initial_simulation_data(arrival_instant=arrival_instant)

    table = simulation_table.table

    table = WebServer.simulate_server_in(table=table, clients=clients,
                                         velocity=velocity)

    table = ApplicationServer.simulate_server_in(table=table, clients=clients,
                                                 velocity=velocity)

    table = DatabaseServer.simulate_server(table=table, clients=clients,
                                           velocity=velocity)

    table = ApplicationServer.simulate_server_out(table=table, clients=clients,
                                                  velocity=velocity)

    table = WebServer.simulate_server_out(table=table, clients=clients,
                                          velocity=velocity)

    print(table)
    save_simulation_csv(table)


clients_number = sys.argv[1] if len(sys.argv) == 2 else 250
print(clients_number)
simulation(clients_number=250)
