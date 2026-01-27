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

ACTIVITIES, NUM_ACTIVITIES, MAX_TIME, MAX_COST = read_file('/Sample Input Files-20260120/input_1000.txt')
# ACTIVITIES, NUM_ACTIVITIES, MAX_TIME, MAX_COST = read_file('/custom_tests/input_small_simple.txt')

assert NUM_ACTIVITIES == len(ACTIVITIES), 'Number of activities stated in file does not match the len of the activities list.'

def add_activity(score_table, activity, depth):
    for i in range(MAX_COST+1):
        if i-activity.cost >= 0:
            inclusion_score = activity.enjoyment + score_table[i-activity.cost][depth].enjoyment
            if inclusion_score > score_table[i][depth].enjoyment:
                score_table[i][depth+1] = ActivitySet(score_table[i-activity.cost][depth].activities + [activity])
            else:
                score_table[i][depth+1] = score_table[i][depth]
        else:
            score_table[i][depth+1] = score_table[i][depth]
    return score_table

score_table = [[ActivitySet([]) for i in range(NUM_ACTIVITIES+1)] for j in range(MAX_COST+1)]
for i in range(NUM_ACTIVITIES):
    score_table = add_activity(score_table, ACTIVITIES[i], i)

print(score_table[-1][-1])
print(score_table[-1][-1].enjoyment)
print(score_table[-1][-1].cost)