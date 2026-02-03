'''
Utilities file for useful functions.
'''

## External Packages ##
import os
from time import perf_counter

## Group Packages ##
from boiler_plates import Activity

def read_file(filename): # File should be in cwd, where filename = '/Sample Input Files-20260120/{input_file}.txt - NOTE: \\ is NOT compatible with Linux so stick with / for routing directories
    '''
    Reads a file and returns: 
        - Activities list, num_activities, max_time, max_budget
    
    Number of activities exists as line 1 but should be compared with len(activities) anyway
    
    :param filename: Path to the input file
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

def run_algorithm(algorithm, input_file):
    '''
    Runs an implementation for the budget problem using a given algorithm
    
    :param algorithm: Function used to solve the problem
    :param input_file: Path to the input file
    '''
    
    ACTIVITIES, NUM_ACTIVITIES, MAX_TIME, MAX_COST = read_file(input_file)
    assert NUM_ACTIVITIES == len(ACTIVITIES), 'Number of activities stated in file does not match the len of the activities list.'

    start = perf_counter()
    activity_set = algorithm(ACTIVITIES, NUM_ACTIVITIES, MAX_TIME, MAX_COST)
    elapsed_time = perf_counter()-start

    activity_str = ''
    for activity in activity_set.activities:
        activity_str += f'- {activity.name} ({activity.time} hours, £{activity.cost}, enjoyment {activity.enjoyment})\n '

    print(f'''
========================================
EVENT PLANNER - RESULTS
========================================
Input File: {input_file}
Available Time: {MAX_TIME} hours (NOT USED)
Available Budget: £{MAX_COST}
--- {algorithm.__name__} ALGORITHM ---
Selected Activities:
 {activity_str}
Total Enjoyment: {activity_set.enjoyment}
Total Time Used: {activity_set.time} hours
Total Cost: £{activity_set.cost}
Execution Time: {elapsed_time} seconds
''')