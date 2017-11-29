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


class ApplicationServer:

    @staticmethod
    def get_processing_time():
        """
            Get Processing time (Duration)
        :return: tuple (duration_ws_in and duration_ws_out)
        """
        return uniform_distribution(40, 60), uniform_distribution(60, 120)
