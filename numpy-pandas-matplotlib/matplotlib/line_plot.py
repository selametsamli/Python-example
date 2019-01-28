import matplotlib.pyplot as plt
import pandas as pd  


df = pd.read_csv("iris.csv")

df1 = df.drop(['Id'],axis=1)

#df1.plot()
#plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species=="Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm, color="red", label = "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm, color="green", label = "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm, color="blue", label = "virginica")


plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

df1.plot(grid = True,linestyle=":")
plt.show()