import numpy as np 

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print("----------")
print(a-b)
print("--------")
print(a**2)

print(np.sin(a))

print(a<2)


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

print(a*b)

#matrix prodcut

a.dot(b.T)

print(np.exp(a))
print("-----------------------")

a = np.random.random((5,5))

print(a)
print("-----------------------")

print(a.sum())
print(a.max())
print(a.min())
print("----------------------")

print(a.sum(axis=0))
print(a.sum(axis=1))
print("----------------------")

print(np.sqrt(a))
print(np.square(a)) #a**2
print("------------------------")

print(np.add(a,a)) # a+a 
