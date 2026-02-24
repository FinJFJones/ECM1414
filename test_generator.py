import random
import matplotlib.pyplot as plt
from performance_test import compare_file

def generate(increments, budget_cap_as_perc, seed=None):
    random.seed(seed)
    str = ''
    total_cost = 0
    with open(f'incremental_tests/scale_test_{0}.txt', 'w') as f:
        f.write(f'{0}\n0 10000\n')
    for i in range(increments):
        with open(f'incremental_tests/scale_test_{i+1}.txt', 'w') as f:
            cost = random.randint(1, 10)
            total_cost += cost
            str += f'activity_{i} 0 {cost} {random.randint(0, 50)}\n'
            f.write(f'{i+1}\n0 {round(total_cost*(budget_cap_as_perc/100))}\n{str}')

