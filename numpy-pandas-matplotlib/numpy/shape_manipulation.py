import numpy as np 


array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
print("------------------")

#flatten
a =array.ravel()
print(a)

array2 = a.reshape(3,3)

arrayT = array2.T
print(arrayT)
print(arrayT.shape)


print("------------------")

array5 = np.array([[1,2],[3,4],[5,6]])
print(array5)
array5.reshape(2,3)
print("reshape: \n",array5)

array5.resize((2,3))
print("resize:\n",array5)