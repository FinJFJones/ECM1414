import test_generator
import matplotlib.pyplot as plt
from performance_test import compare_file

increments = 19

test_generator.generate(19, 0.2)

times_dynamic = []
times_brute_force = []
for i in range(increments+1):
    input_file = f'/incremental_tests/scale_test_{i}.txt'
    dynamic_results, brute_force_results = compare_file(input_file)
    times_dynamic.append(dynamic_results[-1])
    times_brute_force.append(brute_force_results[-1])

plt.plot([i for i in range(increments+1)], times_dynamic)
plt.plot([i for i in range(increments+1)], times_brute_force)
plt.title('Time Taken Per Activity')
plt.xlabel('Activities')
plt.ylabel('Time Taken To Solve')
plt.show()