import pandas as pd 

dictionary = {"Name":['Ali','veli','fikret','selamet','hasan','hayri'],
              'Age':[1,2,3,4,5,6],
              'Maas':[100,200,300,400,500,600] }

dataFrame1 = pd.DataFrame(dictionary)

print(dataFrame1['Age'])
print("-----------------")

print(dataFrame1.Age)
print("-----------------")

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.yeni_feature)
print("-----------------")

print(dataFrame1.loc[:,"Age"])
print("-----------------")

print(dataFrame1.loc[:3,"Age"])
print("-----------------")

print(dataFrame1.loc[:3,"Age":'Maas'])
print("-----------------")

print(dataFrame1.loc[:3 ,['Name','Age']])
print("-----------------")

print(dataFrame1.loc[::-1,:])
print("-----------------")

print(dataFrame1.loc[:,:"Age"])
print("-----------------")

print(dataFrame1.iloc[:,2])

