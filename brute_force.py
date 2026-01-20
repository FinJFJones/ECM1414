'''
Activity dataclass defined in boiler_plates.py
Reading inputs will be standardised for both algorithms in utils.py

Output in form:
return (list of activities), enjoyment, time, cost, constraint_summary
'''

## External Packages ##

## Group Packages ##
from utils import read_file

ACTIVITIES, NUM_ACTIVITIES, MAX_TIME, MAX_BUDGET = read_file('/Sample Input Files-20260120/input_small.txt')

assert NUM_ACTIVITIES == len(ACTIVITIES), 'Number of activities stated in file does not match the len of the activities list.'

