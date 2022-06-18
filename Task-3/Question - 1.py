import numpy as np
start=int(input("First Number : "))
end=int(input("Last Number : "))
Z=np.arange(start,end+1,dtype=int)
print("Input array:")
print(Z)
s = 5
new_vector = np.zeros(len(Z) + (len(Z)-1)*(s))
new_vector[::s+1] = Z
print("\nNew Array with 5 consecutive zeros :")
print(new_vector)
