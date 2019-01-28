import pandas as pd  

df = pd.read_csv("iris.csv")
print(df)

print("column şeyleri\n",df.columns)
print("---------------------------")

print(df.Species.unique())
print("---------------------------")

print("info\n",df.info())
print("---------------------------")

print("describe\n",df.describe())
print("---------------------------")

setosa = df[df.Species == "Iris-setosa"]
print("setosa\n", setosa)
print("---------------------------")

versicolor = df[df.Species=="Iris-versicolor"]
print("versicolor\n",versicolor)
print("---------------------------")

print(setosa.describe())
print(versicolor.describe())