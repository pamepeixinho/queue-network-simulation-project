from enum import Enum, unique


@unique
class InteractionType(Enum):
    """Enum used to describe type of interaction"""
    INTERACTION_ONE = 1
    INTERACTION_TWO = 2
    INTERACTION_THREE = 3
