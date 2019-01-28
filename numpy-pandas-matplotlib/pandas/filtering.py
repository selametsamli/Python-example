import pandas as pd  

dictionary = {"Name":['Ali','veli','fikret','selamet','hasan','hayri'],
              'Age':[1,2,3,4,5,6],
              'Maas':[100,200,300,400,500,600] }

dataFrame1 = pd.DataFrame(dictionary)

filtre1 = dataFrame1.Maas > 200

print("filtre1:\n",filtre1)
print("-----------------------")
print(type(filtre1))

filtrelenmis_data =dataFrame1[filtre1]
print("filtrelenmis_data:\n",filtrelenmis_data)
print("-----------------------")

filtre2 = dataFrame1.Age < 4

iki_filtre = dataFrame1[filtre1 & filtre2]
print("ikili filtreleme: \n",iki_filtre)
print("-----------------------")

print("yaşı 5 den büyük olanı ver:\n",dataFrame1[dataFrame1.Age>5])
