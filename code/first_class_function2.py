def h1(text):
	return '<h1>'+ text + '</h1>'

def h2(text):
	return '<h2>'+ text + '</h2>'

def print_header(func,text):
	return func(text)

print(print_header(h1, "Title 1"))
print(print_header(h2, "Title 2"))
