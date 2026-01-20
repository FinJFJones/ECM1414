'''
Dataclasses for objects with no methods.
'''

from dataclasses import dataclass

@dataclass
class Activity:
    name: int
    time: int # Not accessed - only budget (unless extension)
    cost: int
    enjoyment: int