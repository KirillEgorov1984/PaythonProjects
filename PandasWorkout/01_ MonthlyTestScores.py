import pandas as pd
import numpy as np

g = np.random.default_rng(0)
months = 'Sep Oct Nov Dec Jan Feb Mar Apr May Jun'.split()
s = pd.Series(g.integers(70, 101, 10),index=months)
print(f'Yearly average: {s.mean()}')
first_half_average = s['Sep':'Jan'].mean()
second_half_average = s['Feb':'Jun'].mean()
print(f'First half average: {first_half_average}')
print(f'Second half average: {second_half_average}')
print(f'Improvement: {second_half_average - first_half_average}')