import pandas as pd
import numpy as np

g = np.random.default_rng(0) #через numpy возвращает массив состоящий из случайных чисел
months = 'Sep Oct Nov Dec Jan Feb Mar Apr May Jun'.split()
s = pd.Series(g.integers(70, 101, 10),index=months)

print(months)
print(s)

first_half_average = s['Sep':'Jan'].mean()
second_half_average = s['Feb':'Jun'].mean()
print(f'Yearly average: {s.mean()}')# средняя оценка студента за тесты за весь год
print(f'First half average: {first_half_average}')# средняя оценка студента за перове полугодие
print(f'Second half average: {second_half_average}') # средняя оценка студента за второе полугодие
print(f'Improvement: {second_half_average - first_half_average}') #успеваемость повысмлась или нет
print(f'Max: {s.idxmax()}') #макс оценка в каком месяце
print(f'Perfect: {s.sort_values(ascending=False).head(5)}') #пять лучших оценок
print(f'Round: {s.round(-1)}') #округляем до десятичной точки

