import numpy as np


array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) #1*15 vector

print(array.shape)

a = array.reshape(3,5)
print("shape: ",a.shape)
print("dimension: ",a.ndim)

print("data type: ",a.dtype.name)
print("size: ",a.size)

print("type: ",type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

zeros = np.zeros((3,4))

zeros[0,0]=5
print(zeros)

ones = np.ones((3,4)) 

empty = np.empty((3,4)) # boş dizi oluşturur
print(empty)
print("--------------------")
a = np.arange(10,50,5)

print(a)

a = np.linspace(0,50,20) # 10 dan 50 ye kadar araya 20 ssayı yazar

print(a)
