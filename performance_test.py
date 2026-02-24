'''
As per 6.1 in the spec, we need to compare performance of both

This file runs and compares algorithms with ALL given inputs as the performance advantage may swing based on input complexity
'''

from dynamic import dynamic_algorithm
from brute_force import brute_force_algorithm
from utils import run_algorithm

def compare_file(input_file):
    enjoyment_d, time_d, cost_d, elapsed_time_d = run_algorithm(dynamic_algorithm, input_file)
    enjoyment_bf, time_bf, cost_bf, elapsed_time_bf = run_algorithm(brute_force_algorithm, input_file)

    return [enjoyment_d, time_d, cost_d, elapsed_time_d], [enjoyment_bf, time_bf, cost_bf, elapsed_time_bf]

compare_file('/Sample Input Files-20260120/input_small.txt')