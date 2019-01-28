import numpy as np 

liste=[1,2,3,4] #list

array = np.array(liste) #np.array 


print(array)

liste2 = list(array) #array to liste


a = np.array([1,2,3])
b = a
c = a

b[0] = 5

print("a:\n",a)
print("b:\n",b)
print("c:\n",c)
print("-----------------------")


d = np.array([1,2,3])
e = d.copy()
f = d.copy()
f[0] = 5

print("d:\n",d)
print("e:\n",e)
print("f:\n",f)