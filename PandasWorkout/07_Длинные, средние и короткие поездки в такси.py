import pandas as pd
import numpy as np

s = pd.read_csv('c:\\MyWork\\PaythonProjects\\PandasWorkout\\data\\taxi-passenger-count.csv'
                ,
                header=None).squeeze()

print(s)

bins_seporate = pd.cut(s,
      bins=[0,2,4,s.max()],
      include_lowest=True,
      labels=['short', 'medium','long']).value_counts()

print(bins_seporate)

print(s.max())

print(s.describe())

pas_count = pd.cut(s[s  == 1],
      bins=3,
      labels=['short', 'medium','long'], retbins=True)[-1]
print(pas_count)