import pandas as pd
import numpy as np

s = pd.Series('1234 5678 9012'.split(),dtype=np.int64)
print(s.mean())
