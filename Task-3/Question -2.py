import numpy as np
arr1 = np.random.randint(0,2,6)
print("First array:")
print(arr1)
arr2 = np.random.randint(0,2,6)
print("Second array:")
print(arr2)
arrayeql = np.allclose(arr1, arr2)
print(arrayeql)
