def foo(msg):	
	def bar():
		print(msg)
	return bar
hi_f = foo('hi')
bye_f = foo('bye')

hi_f()
bye_f()


#print(f.__name__)


