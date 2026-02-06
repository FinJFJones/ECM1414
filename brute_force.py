'''
This file contains algorithms for a brute force implementation of a budget allocation problem.
'''

## External Packages ##

## Group Packages ##
from boiler_plates import ActivitySet

def best_activity(activities, num_activities, current_activities, max_cost):
    '''
    A recursive solution to find the activities with the most enjoyment within the budget
    
    :param activities: List of activities
    :param num_activities: Number of activities
    :param current_activities: Array of current activities found
    :param max_cost: Budget constraint
    :return: Set of activities that match the result
    :rtype: ActivitySet
    '''

    top_activity = ActivitySet(current_activities) #hold best activity, also initialised in case of all activities have been explored

    for activity in activities: #loop through all the activities so they can all be visited atleast once
        if activity in current_activities: #we cannot repeat activities so skip these
            continue
        new_activity_set = ActivitySet(current_activities + [activity]) #use for checking constraint and passing recursively
        if new_activity_set.cost > max_cost:
            continue
        activity_found = best_activity(activities, num_activities, new_activity_set.activities, max_cost) #recursively call algorithm and use the new activities
        if activity_found.enjoyment > top_activity.enjoyment: #if better activity make it the best one with best enjoyment
            top_activity = activity_found

    return top_activity

def brute_force_algorithm(activities, num_activities, max_time, max_cost):
    '''
    Implementation of a brute force programming solution to a budgeting task.
    
    :param activities: List of activities
    :param num_activities: Number of activities
    :param max_time: Time constraint
    :param max_cost: Budget constraint
    :return: Set of activities
    :rtype: ActivitySet
    '''

    return best_activity(activities, num_activities, [], max_cost) #calls the algorithm which will recursively search in itself
