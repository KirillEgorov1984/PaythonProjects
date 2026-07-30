import pandas as pd
import numpy as np

days = 'Sun Mon Tue Wed Thu Fri Sat'.split()

g = np.random.default_rng(0)
s = pd.Series(g.normal(20,5,28), index=days*4).round().astype(np.int8)

s.loc['Mon'].mean()

print(s)
print(s.loc['Mon'].mean()) # расчет среднего по Mon
print(s[['Sun', 'Sat']].mean()) #средняя температура на выходных в субботу и воскресенье
print(s[s.diff()>2])#Сколько раз темепература отличалась более чем на два градуса по сравнению с предыдущим днем
print(s.value_counts().head(2)) #Какая температура встречалась в нашем наборе данных чаше остальных ? Сколько раз на появлялась



