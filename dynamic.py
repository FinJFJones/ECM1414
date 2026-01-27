'''
Activity dataclass defined in boiler_plates.py
Reading inputs will be standardised for both algorithms in utils.py

Variables needed in this file (and brute_force.py):
    - Maximum budget
    - Maximum time (only for possible extension)
    - A list of activities using the Activity dataclass


'''

## External Packages ##

## Group Packages ##
from utils import read_file
from boiler_plates import ActivitySet

ACTIVITIES, NUM_ACTIVITIES, MAX_TIME, MAX_BUDGET = read_file('/Sample Input Files-20260120/input_small.txt')

assert NUM_ACTIVITIES == len(ACTIVITIES), 'Number of activities stated in file does not match the len of the activities list.'

'''
Example Activities
0 = Activity(name='Campus-Tour', time=2, cost=20, enjoyment=50)
1 = Activity(name='Game-Night', time=3, cost=80, enjoyment=120)
2 = Activity(name='Museum-Trip', time=4, cost=100, enjoyment=150)
3 = Activity(name='Pizza-Workshop', time=2, cost=60, enjoyment=100)
4 = Activity(name='Hiking', time=5, cost=30, enjoyment=140)
'''

def should_include(stored_values, index, original_index, activity):
    if MAX_BUDGET-stored_values[index].cost >= activity.cost:
        if stored_values[index].enjoyment + activity.enjoyment > stored_values[original_index].enjoyment:
            stored_values[original_index] = [] # TODO: this should set the original index of stored_values to the current index with activity added
    elif index != 0:
        return should_include(stored_values, index-1, original_index, activity)
    return stored_values

stored_values = [ActivitySet([])] # index 0 represents [], index 1 only activity A, then B, etc.
for i in range(len(ACTIVITIES)):
    tested_activity = ACTIVITIES[i]
    stored_values = should_include(stored_values, i, i, tested_activity)




    # Exclude value = max_vals[i]
    # Include value = max_vals[i] if space or rerun for max_vals[i-1]
    # Therefore max_vals needs info on how much constraint used
    #if should_include(MAX_BUDGET, max_vals, constraints_used, i, i, tested_activity):


