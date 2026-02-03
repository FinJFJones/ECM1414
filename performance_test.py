'''
As per 6.1 in the spec, we need to compare performance of both

This file runs and compares algorithms with ALL given inputs as the performance advantage may swing based on input complexity
'''

from dynamic import dynamic_algorithm
from brute_force import brute_force_algorithm
from utils import run_algorithm

input_file = '/Sample Input Files-20260120/input_small.txt'

run_algorithm(dynamic_algorithm, input_file)

run_algorithm(brute_force_algorithm, input_file)


