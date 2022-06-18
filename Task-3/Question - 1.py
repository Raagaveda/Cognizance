import numpy as np
Z=np.arange(10,15)
print("Original array:")
print(Z)
p = 5
new_Z = np.zeros(len(Z) + (len(Z)-1)*(p))
new_Z[::p+1] = Z
print("\nNew array:")
print(new_Z)
