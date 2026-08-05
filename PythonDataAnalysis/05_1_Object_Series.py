import pandas as pd
from pandas import RangeIndex

obj =pd.Series([4,7,-5,3])
#print(obj)# пример объекта Series

obj_array = obj.array
obj.index
RangeIndex(start=0,stop=4,step=1)

#print(obj_array)

obj2 = pd.Series([4,7,-5,3], index=['a','b','c','d'])
print(obj2)

sata = {"Ohio":35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000} #создание словаря
obj4 = pd.Series(sata)
print(obj4)

# преобразование обїекта Series обратно в словарь

print(obj4.to_dict())# to_dict преобразует Series в словарь