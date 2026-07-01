import pandas as pd
import numpy as np

g = np.random.default_rng(0)
months = 'Sep Oct Nov Dec Jan Feb Mar Apr May Jun'.split()
s = pd.Series(g.integers(40, 61, 10),index=months)
avg_score = 80 - s.mean()
scaling = f'({s + avg_score})'

Z = s[0:]
W = s[s > 50]
A = s[s > s.mean() + s.std()]
B = s[(s < s.mean() + s.std())&(s > s.mean())]
C = s[(s > s.mean() - s.std())&(s < s.mean())]
D = s[s < s.mean() - s.std()]

#print(avg_score)
#print(scaling)
print(A)
print(B)
print(C)
print(D)
print(s)
print(W)

# Встертились ли нам оценки больше или меньше средней оценки на два стандартных отклонения и более ?
E = s[(s < s.mean()-2*s.std()) | (s > s.mean()+2*s.std())]

print(E)

smean = s.mean()
smedian = s.median()

print(smean, smedian)
