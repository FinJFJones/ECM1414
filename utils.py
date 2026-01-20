'''
Utilities file for useful functions.
'''

## External Packages ##
import os

## Group Packages ##
from boiler_plates import Activity

def read_file(filename): # File should be in cwd
    '''
    Reads a file and returns: 
        - Activities list, max_time, max_budget
    
    Number of activities exists as line 1 but can be be inferred from len(activities) anyway
    '''
    
    path = os.getcwd() + filename

    with open(path, 'r') as file:
        lines = file.read().splitlines()
        activities_lines = lines[2:]
        time_cost_line = lines[1]
        max_time = int(time_cost_line.split()[0])
        max_cost = int(time_cost_line.split()[1])
    
    activity_list = []
    for line in activities_lines:
        data = line.split()
        activity = Activity.from_strings(data)
        activity_list.append(activity)
    
    return activity_list, max_time, max_cost

print(read_file('/Sample Input Files-20260120/input_small.txt')) # Example func test