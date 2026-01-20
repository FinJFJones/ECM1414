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

ACTIVITIES, NUM_ACTIVITIES, MAX_TIME, MAX_BUDGET = read_file('/Sample Input Files-20260120/input_small.txt')

assert NUM_ACTIVITIES == len(ACTIVITIES), 'Number of activities stated in file does not match the len of the activities list.'

'''
Approach:
Activity 1 -> Activity 2 = Activity 2 -> Activity 1
Therefore, timetable can be represented as a set as order doesn't matter

As order is irrelevant, each activity is binary (either include or don't include)

Activities where cost > budget can be discounted

Activities where budget x = budget y but enjoyment x > enjoyment y can be discounted unless there is spare budget, but regardless x should always be preferred/tested first over y

Activities can be ranked by enjoyment/budget. High ratios should be tested first.
'''