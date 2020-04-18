#files =[]
#for x in range(10000):
#	files.append(open('files/'+str(x),'w'))


'''
Method 1: Using Class
'''

class open_ng():
	def __init__(self,filename,mode):
		self.filename = filename
		self.mode = mode

	def __enter__(self):
		self.file = open(self.filename,self.mode)
		return self.file
	def __exit__(self, exc_type, exc_val, traceback):
		self.file.close()

with open_ng('test.txt','w') as fd:
	fd.write("Testing with class...")

#print(fd.closed)

'''
Method 2 : Using Context Manager
'''

from contextlib import contextmanager

@contextmanager
def open_ng2(filename,node):
	fd = open(filename,mode)
	yield fd
	fd.close()
with open_ng('test.txt','w') as fd:
	fd.write('Testing with context manager...')

print(fd.closed)
