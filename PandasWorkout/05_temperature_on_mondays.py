import pandas as pd
import numpy as np

days = 'Sun Mon Tue Wed Thu Fri Sat'.split()

g = np.random.default_rng(0)
s = pd.Series(g.normal(20,5,28), index=days*4).round().astype(np.int8)

s.loc['Mon'].mean()

print(s)
print(s.loc['Mon'].mean()) # расчет среднего по Mon



