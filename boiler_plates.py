'''
Dataclasses to simplify how activities are stored.
'''

from dataclasses import dataclass

@dataclass
class Activity:
    '''
    Dataclass containing an Activity's name, time taken, cost and enjoyment
    '''
    
    name: str
    time: int # Not accessed - only cost (unless extension)
    cost: int
    enjoyment: int
    id: int

    @classmethod
    def from_strings(cls, data, id):
        return cls(data[0], int(data[1]), int(data[2]), int(data[3]), id)

@dataclass
class ActivitySet:
    '''
    Dataclass containing a list of activities which can return total enjoyment, time and cost
    '''

    activities: list # List of activities

    @property
    def enjoyment(self):
        return sum(activity.enjoyment for activity in self.activities)
    
    @property
    def time(self):
        return sum(activity.time for activity in self.activities)

    @property
    def cost(self):
        return sum(activity.cost for activity in self.activities)
    
