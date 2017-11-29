"""
    Firewall

    Function: Calculate processing time BY INTERACTION

    Problem Desc: "Considere que algumas transações envolvem questões de segurança e que,
    portanto, precisam passar por processos de autentificação. Estes processos ocorrem
    junto a um Firewall. Os acessos ao site envolvendo processamento relativos a
    segurança referem-se especificamente as interações do tipo 2 ou 3. Numa interação
    tipo 2, o processamento dura algo entre 3 mseg e 5 mseg já no processamento de uma
    interação tipo 3, este dura algo entre 7 mseg e 10 mseg."
"""
from UniformDistribution import uniform_distribution

from InteractionType import InteractionType


class Firewall:

    @staticmethod
    def get_processing_time(interaction_type):
        if interaction_type == InteractionType.INTERACTION_TWO:
            min_value, max_value = 3, 5
        else:
            min_value, max_value = 7, 10
        return uniform_distribution(min_value, max_value)
