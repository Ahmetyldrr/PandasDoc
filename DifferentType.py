import pandas as pd
import numpy as np

df2 = pd.DataFrame({
 'A': 1.,
 'B': ['x','y','z','m'],
 'C': pd.Series(1, index=list(range(4)), dtype='float32'),
 'D': np.array([3] * 4, dtype='int32'),
 'E': pd.Categorical(["test", "train", "tes", "train"]),
 'F': 'foo',

  'G':  [12,23,31,44]

 })



print(df2)
print(df2.dtypes)
print(df2.columns.values)
print(df2.tail(1))
print('========numpy seti================')
print(df2.to_numpy())

print('=========tanımlama==============')
print(df2.describe())

print('==========sıralama==============')

print(df2.sort_values(by='G',ascending=False))

print('===========G sutunu==============')
print(df2['G'])

print('===========ilk 3 satır=============')
print(df2[0:3])


print('===========A ve G sutun al=============')
print(df2.loc[:, ['A', 'G']])


print('===========ikili filtre=============')
print(df2.loc['x':'z', ['B', 'G']])


print('===========ikili filtre=============')

print(df2.iloc[3:5, 0:2])

print('===========çoklu filtre=============')
print(df2.iloc[[0, 2], [2, 3]])



print('===========tüm sutun iki satır=============')
print(df2.iloc[1:3, :])


print('===========ttüm satır sutun seç=============')
print(df2.iloc[:, 1:3])


print('===========değere göre filtreleme=============')
print(df2[df2['G'] > 25])



print('===========hücre değerine göre çoklu seçim=============')
print(df2[df2['E'].isin(['train','test'])])
























