import pandas as pd
import numpy as np


s = pd.read_csv('/PandasWorkout/data/taxi-passenger-count.csv',
                header=None).squeeze()

print(s.loc[s==1].count()) # количество поездок в такси с 1им поссажиром
print(s.loc[s==6].count()) # количество поездок в такси с 6ю поссажирами

One=s.loc[s==1].count()/s.count()*100
Six=s.loc[s==6].count()/s.count()*100
OneSix = s.value_counts(normalize=True)[[1,6]]*100
print(OneSix)
print(One)
print(Six)

print(s.quantile([.25,.50,.75]))
print(s.value_counts(normalize=True)[[3,4,5,6]].sum()) # какой процент перевозок троих, четверых, пятерых и шестярых пассажиров