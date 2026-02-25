import test_generator
import matplotlib.pyplot as plt
from performance_test import compare_file

test_used = 1000
input_file = f'/incremental_tests/scale_test_{test_used}.txt'

times_dynamic = []
times_brute_force = []
for i in range(101):
    test_generator.generate(test_used, i, 42)
    
    dynamic_results, brute_force_results = compare_file(input_file)
    times_dynamic.append(dynamic_results[-1])
    times_brute_force.append(brute_force_results[-1])

plt.plot([i for i in range(101)], times_dynamic, label='Dynamic')
plt.plot([i for i in range(101)], times_brute_force, label='Brute Force')
plt.legend()
plt.title('Time Taken Per Budget')
plt.xlabel('Budget as a % of cost of all activities')
plt.ylabel('Time Taken To Solve')
plt.show()