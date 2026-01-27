'''
As per 6.1 in the spec, we need to compare performance of both

time.perf_counter is best for time comparisons in this case
(I imagine a parallel threading race is overkill for this task)

This file should run and compare algorithms with ALL given inputs as the performance advantage may swing based on input complexity
'''

from dynamic import dynamic_algorithm
# from brute_force import brute_force_algorithm
from time import perf_counter

start = perf_counter()
activity_set = dynamic_algorithm()
time_difference = perf_counter()-start
print(time_difference)

start = perf_counter()
# activity_set = brute_force()
time_difference = perf_counter()-start
print(time_difference)
