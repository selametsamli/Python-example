import matplotlib.pyplot as plt
import pandas as pd  
import numpy as np 


#x = np.array([1,2,3,4,5,6,7])
#y = x*2+5

#plt.bar(x,y)
#plt.title("bar plot")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()


x = np.array([1,2,3,4,5,6,7])
a = ["turkey","use","germany","ita","fra","kat","fiko"]
y = x*2+5

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()