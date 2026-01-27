'''
Activity dataclass defined in boiler_plates.py
Reading inputs will be standardised for both algorithms in utils.py

Variables needed in this file (and brute_force.py):
    - Maximum budget
    - Maximum cost (only for possible extension)
    - A list of activities using the Activity dataclass
'''

## External Packages ##

## Group Packages ##
from utils import read_file
from boiler_plates import ActivitySet

ACTIVITIES, NUM_ACTIVITIES, MAX_TIME, MAX_COST = read_file('/Sample Input Files-20260120/input_1000.txt')
# ACTIVITIES, NUM_ACTIVITIES, MAX_cost, MAX_COST = read_file('/custom_tests/input_small_simple.txt')

assert NUM_ACTIVITIES == len(ACTIVITIES), 'Number of activities stated in file does not match the len of the activities list.'

def add_activity(score_table, activity, depth):
    for i in range(MAX_COST+1): # For logging enjoyment from 0 budget to the max budget
        if i-activity.cost >= 0: # If there is budget, add this activity
            inclusion_score = activity.enjoyment + score_table[i-activity.cost][depth].enjoyment # Remove current activity from the budget, then add the best case from the remaining budget
            if inclusion_score > score_table[i][depth].enjoyment: # If the new enjoyment value is better, use that
                score_table[i][depth+1] = ActivitySet(score_table[i-activity.cost][depth].activities + [activity])
            else:
                score_table[i][depth+1] = score_table[i][depth] # Keep previous score
        else:
            score_table[i][depth+1] = score_table[i][depth] # Keep previous score
    return score_table # Return the new table

def dynamic_algorithm():
    score_table = [[ActivitySet([]) for i in range(NUM_ACTIVITIES+1)] for j in range(MAX_COST+1)] # Create a grid recording the best activity sets
    for i in range(NUM_ACTIVITIES): # Loop to build up each activity
        score_table = add_activity(score_table, ACTIVITIES[i], i) # Find max enjoyment for every constraint up to the max_cost
    return score_table[-1][-1] # Return final enjoyment
