'''
Utilities file for useful functions.
'''

## External Packages ##
import os

## Group Packages ##
from boiler_plates import Activity

def read_file(filename): # File should be in cwd, where filename = '/Sample Input Files-20260120/{input_file}.txt - NOTE: \\ is NOT compatible with Linux so stick with / for routing directories
    '''
    Reads a file and returns: 
        - Activities list, num_activities, max_time, max_budget
    
    Number of activities exists as line 1 but should be compared with len(activities) anyway
    '''
    
    path = os.getcwd() + filename

    with open(path, 'r') as file:
        lines = file.read().splitlines() # Better than readlines, prevents \n existing at the end of lines
        activities_lines = lines[2:] # First 2 lines used for constraints
        num_activities = int(lines[0]) # First line
        time_cost_line = lines[1] # Second line lists both constraints
        max_time = int(time_cost_line.split()[0]) # Time and cost separated by whitespace
        max_cost = int(time_cost_line.split()[1])
    
    activity_list = []
    for line in activities_lines:
        data = line.split() # Activity line split into name, time, cost, enjoyment
        activity = Activity.from_strings(data) # Uses class method for casting
        activity_list.append(activity)
    
    return activity_list, num_activities, max_time, max_cost