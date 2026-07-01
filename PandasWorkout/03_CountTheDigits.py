import pandas as pd
import numpy as np

g = np.random.default_rng(0)
s = pd.Series(g.integers(0,100,10))
s_final = s // 10 #вариант 1


s_final2 = (
    s.astype(str) # преобразование массива даных в тип стринг# #
    .str.get(-2)# извлекаем второй символ с конца
     .fillna('0') # Заменяем NaN на '0'
     .astype(np.int8) # преобразуем результат в тип данных int8
)

print (s_final)
print (s_final2)

print(s.min(), s.max())
print(s.astype(np.int8))
print(s.astype(np.uint8))
print(s.astype(np.int16))


ss = pd.Series(np.random.rand(10) * 1000)
index_mask = ss[ss.astype(np.int64) % 2 == 0]
print(index_mask)
