import numpy as np  
a = [1,2,3,4,5,6]
a = np.reshape(a,(2,3))
a = a.tolist()
print(np.median(a[1]))