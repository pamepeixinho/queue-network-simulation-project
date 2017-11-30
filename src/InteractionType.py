from enum import IntEnum, unique


@unique
class InteractionType(IntEnum):
    """Enum used to describe type of interaction"""
    INTERACTION_ONE = 1
    INTERACTION_TWO = 2
    INTERACTION_THREE = 3
