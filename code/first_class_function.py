def h1(text):
	return '<h1>' + text + '</h1>'

print(h1('title'))

print_h1 = h1('title') # <h1>title</h1>
print(type(print_h1)) # <type 'str'>


print_h1 = h1
print(type(print_h1)) # <type 'function'> 

