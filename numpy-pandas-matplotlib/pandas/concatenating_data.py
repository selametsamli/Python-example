import pandas as pd


dictionary = {"Name":['Ali','veli','fikret','selamet','hasan','hayri'],
              'Age':[1,2,3,4,5,6],
              'Maas':[100,200,300,400,500,600] }

dataFrame1 = pd.DataFrame(dictionary)
dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]

dataFrame1.drop(["yeni_feature"],axis=1, inplace = True)

print(dataFrame1)
print("---------------------")

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical
data_concat = pd.concat([data1,data2],axis=0)
print("data_concat:\n",data_concat)
print("---------------------")

#horizontal

maas = dataFrame1.Maas
age = dataFrame1.Age

data_h_concat = pd.concat([maas,age],axis=1)
print("data_h_concat:\n",data_h_concat)