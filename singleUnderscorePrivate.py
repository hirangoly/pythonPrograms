# Use one leading underscore to indicate a private variable or method. But yes, it is still accessible, python doesn't have real private variables. Basically a leading underscore just means that method is not part of your class or module api.

class A():
	def _singleundeescorefunc(self):
		print 'I am single underscore func'

	def __doubleunderscorefunc(self):
		print 'I am double underscore func'


a=A()
# it is still accessible, python doesn't have real private variables
a._singleundeescorefunc()
# you can't call double underscore directly - see double underscore example, how to call it
#a.__doubleunderscorefunc()


