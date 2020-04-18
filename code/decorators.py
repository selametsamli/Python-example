from time import sleep
from time import time
import random

#def machine_learner(training_set):
#	x = random.randint(1,10)
#	print('~ Learning for {}'.format(training_set))
#	print('Random number: {}'.format(x))
#	sleep(x)


def timer(func):
	def f(*args, **kwargs):
		before = time()
		func(*args, **kwargs)
		after = time()

		print('Bekleme Süresi: ',after-before)
	return f

@timer
def machine_learner(training_set):
	x = random.randint(1,10)
	print('~Learning for {}'.format(training_set))
	print('Random number: {}'.format(x))
	sleep(x)

#before = time()
#machine_learner(15)
#after = time()
#print('Bekleme süresi', after-before)

#before = time()
#machine_learner(15)
#after = time()
#print('Bekleme süresi', after-before)

#f1 = timer(machine_learner)
#f1(5)
#f1(12)


machine_learner(15)

machine_learner(22)
