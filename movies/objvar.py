# Filename: objvar.py

def sayHi():
	print 'Hello,world'

class Person:
	'''Represents a person.'''
	population = 0
	
	def __init__(self, name):
		'''Initializes the person's data.'''
		self.name = name
		print '(Initializeing %s)' % self.name
		
		# When this person is created,he/she
		# adds to thpopulation
		Person.population += 1
		
	def __del__(self):
		'''I am dying.'''
		print '%s says bye.' % self.name
		
		Person.population -= 1
		
		if Person.population == 0:
			print 'I am the last one.'
		else:
			print 'There are still %d pepole left.' % Person.population
			
	def sayHi(self):
		'''Greeting by the person.
		
		Really, that's all it does.'''
		print 'Hi, my name is %s.' % self.name
	
	def howMany(self):
		'''Prints the current population.'''
		if Person.population == 1:
			print 'I am the only person here.'
		else:
			print 'We have %d persons here.' % Person.population
			

	