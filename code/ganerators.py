from time import sleep

def compute():
	result = []
	
	for i in range(10):
		sleep(.5) # hesaplama gerekiren kısım.
		result.append(i**3)
	return result

def compute2():
	for i in range(10):
		sleep(.5)
		yield i**3


#print(compute())
for res in compute2():
	print(res)
