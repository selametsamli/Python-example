import pandas as pd


dictionary = {"Name":['Ali','veli','fikret','selamet','hasan','hayri'],
              'Age':[1,2,3,4,5,6],
              'Maas':[100,200,300,400,500,600] }

dataFrame1 = pd.DataFrame(dictionary)

ortalama_maas = dataFrame1.Maas.mean()
print("Ortalam Maas: ",ortalama_maas)
print("----------------------------")

dataFrame1['Maas Seviyesi'] = ["yuksek" if ortalama_maas < each else "dusuk" for each in dataFrame1.Maas]

print(dataFrame1)
print("----------------------------")


dataFrame1.columns = [ each.lower() for each in dataFrame1.columns] # büyük harfleri küçültür
print(dataFrame1)
print("----------------------------")

dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if (len(each.split())>1) else each for each in dataFrame1.columns]
print(dataFrame1)