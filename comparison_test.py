import test_generator
import matplotlib.pyplot as plt
from performance_test import compare_file

increments = 500

test_generator.generate(increments, 50)

times_dynamic = []
times_brute_force = []
for i in range(increments+1):
    input_file = f'/incremental_tests/scale_test_{i}.txt'
    dynamic_results, brute_force_results = compare_file(input_file)
    times_dynamic.append(dynamic_results[-1])
    times_brute_force.append(brute_force_results[-1])

plt.plot([i for i in range(increments+1)], times_dynamic, label='Dynamic')
plt.plot([i for i in range(increments+1)], times_brute_force, label='Brute Force')
plt.legend()
plt.title('Time Taken Per No. Activities')
plt.xlabel('Activities')
plt.ylabel('Time Taken To Solve (s)')
plt.show()