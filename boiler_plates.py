'''
Dataclasses for objects with no methods.
'''

from dataclasses import dataclass

@dataclass
class Activity:
    '''
    Dataclass containing an Activitie's name, time taken, cost and enjoyment
    '''
    
    name: str
    time: int # Not accessed - only budget (unless extension)
    cost: int
    enjoyment: int

    @classmethod
    def from_strings(cls, data):
        return cls(data[0], int(data[1]), int(data[2]), int(data[3]))
    