import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])


print(s)
print(s.fillna('boş'))
print(s.values.reshape(3,2))



