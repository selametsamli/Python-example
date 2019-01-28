import matplotlib.pyplot as plt
import pandas as pd  


df = pd.read_csv("iris.csv")

df1 = df.drop(['Id'],axis=1)

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species=="Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color ="red", label = "setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color ="green", label = "versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color ="blue", label = "virginica")


plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()