"""
    Database server, also known as DB in the problem description

    Function: Calculate processing time of messages in this server

    Problem Desc: "O tempo de processamento no servidor de banco de dados (nó sete da interação tipo 3)
     se divide em duas parcelas, ambas uniformemente distribuídas. Entre 15 mseg e 30 mseg
     de processamento e entre 50 mseg e 400 mseg de acesso a disco."
"""
from src.UniformDistribution import uniform_distribution


class DatabaseServer:
    @staticmethod
    def get_processing_time():
        """
            Get Processing time (Duration)
        :return: tuple (duration_ws_in and duration_ws_out)
        """
        return uniform_distribution(15, 30) + uniform_distribution(50, 400)
