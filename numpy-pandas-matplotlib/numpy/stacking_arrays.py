import numpy as np 

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])
print("array1:\n",array1)
print("array2:\n",array2)

array3 = np.vstack((array1,array2))

print("vercial:\n",array3)

array4 = np.hstack((array1,array2))
print("horizontal:\n",array4)