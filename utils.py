'''
Utilities file for useful functions.
'''

import os

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
        time_budget_line = lines[1]
        time = time_budget_line.split()[0]
        budget = time_budget_line.split()[1]
    
    for line in activities_lines:
        pass # TODO: finish defining activities from the dataclass