'''
This file contains algorithms for a dynamic programming implementation of a budget allocation problem.
'''

## External Packages ##

## Group Packages ##
from utils import read_file
from boiler_plates import ActivitySet

def add_activity(score_table, activity, depth, max_cost):
    '''
    Builds up the optimal solution for this activity and it's predecessors including all constraints up to the max contraint
    
    :param score_table: Table with max_enjoyments
    :param activity: Activity being added
    :param depth: Number of current added activities
    :param max_cost: Constraint
    '''

    for i in range(max_cost+1): # For logging enjoyment from 0 budget to the max budget
        if i-activity.cost >= 0: # If there is budget, add this activity
            inclusion_score = activity.enjoyment + score_table[i-activity.cost][depth].enjoyment # Remove current activity from the budget, then add the best case from the remaining budget
            if inclusion_score > score_table[i][depth].enjoyment: # If the new enjoyment value is better, use that
                score_table[i][depth+1] = ActivitySet(score_table[i-activity.cost][depth].activities + [activity])
            else:
                score_table[i][depth+1] = score_table[i][depth] # Keep previous score
        else:
            score_table[i][depth+1] = score_table[i][depth] # Keep previous score
    return score_table # Return the new table

def dynamic_algorithm(activities, num_activities, max_time, max_cost):
    '''
    Implementation of a dynamic programming solution to a budgeting task.
    
    :param activities: List of activities
    :param num_activities: Number of activities
    :param max_time: Time constraint
    :param max_cost: Budget constraint
    :return: Set of activities
    :rtype: ActivitySet
    '''
    
    score_table = [[ActivitySet([]) for i in range(num_activities+1)] for j in range(max_cost+1)] # Create a grid recording the best activity sets
    for i in range(num_activities): # Loop to build up each activity
        score_table = add_activity(score_table, activities[i], i, max_cost) # Find max enjoyment for every constraint up to the max_cost
    return score_table[-1][-1] # Return final enjoyment
