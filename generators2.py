import time

def compute():
	result =[]
	
	for i in range(1000000):
		result.append(i**3)
	return result

def compute2():
	for i in range(1000000):
		yield i**3

t1 = time.process_time()
res1 = compute()
t2 = time.process_time()

print("res1 {} saniye.".format(t2-t1))

t1 = time.process_time()
res2 = compute2()
t2 = time.process_time()
print("res2 {} saniye".format(t2-t1))
