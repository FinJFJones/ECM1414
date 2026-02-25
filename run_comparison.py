'''
As per 6.1 in the spec, we need to compare performance of both

This file runs and compares algorithms with ALL given inputs as the performance advantage may swing based on input complexity
'''

import sys

from dynamic import dynamic_algorithm
from brute_force import brute_force_algorithm
from utils import run_algorithm


if len(sys.argv) > 1:
    run_algorithm(dynamic_algorithm, sys.argv[1])
    run_algorithm(brute_force_algorithm, sys.argv[1])
else:
    print('No input file path provided')