'''
As per 6.1 in the spec, we need to compare performance of both

time.perf_counter is best for time comparisons in this case
(I imagine a parallel threading race is overkill for this task)

This file should run and compare algorithms with ALL given inputs as the performance advantage may swing based on input complexity
'''

from dynamic import dynamic_algorithm
# from brute_force import brute_force_algorithm
from utils import run_algorithm

run_algorithm(dynamic_algorithm, '/Sample Input Files-20260120/input_small.txt')
