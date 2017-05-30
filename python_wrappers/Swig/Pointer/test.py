import modarray

import numpy as np

l=np.arange(1000,dtype=np.float32)
tab = [1,2,3,4]
result = modarray.array_sum(l)
print(result)
result = modarray.array_sum(tab)
print(result)

