import pandas as pd


dictionary = {"Name":['Ali','veli','fikret','selamet','hasan','hayri'],
              'Age':[1,2,3,4,5,6],
              'Maas':[100,200,300,400,500,600] }

dataFrame1 = pd.DataFrame(dictionary)
dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]

dataFrame1["list_comp"] = [each*2 for each in dataFrame1.Age]

print(dataFrame1)
print("---------------------------")

#apply()

def multiply(age):
    return age*2

dataFrame1["apply_methodu"] = dataFrame1.Age.apply(multiply)


print(dataFrame1)