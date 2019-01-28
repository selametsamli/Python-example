import matplotlib.pyplot as plt
import pandas as pd  


df = pd.read_csv("iris.csv")

df1 = df.drop(['Id'],axis=1)

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species=="Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.hist(setosa.PetalLengthCm, bins = 30)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()