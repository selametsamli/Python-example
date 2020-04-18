def f1(param):
	def f2():
		print(param)
		return
	return f2

f = f1('My param')
print(type(f)) # <type 'function'>
f() # my param
