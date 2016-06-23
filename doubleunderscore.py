class A(object):
	# function cannpt be override in subclass
	def __NoOverrideFunc(self):
		print 'I am a function from class A, cannot be override'

	def CallNoOverrideFun(self):
		self.__NoOverrideFunc()

	def CallSimpleFun(self):
		self.funComm()

	def funComm(self):
		print 'this is a simple func A'

class B(A):
	def __NoOverrideFunc(self):
		print 'I am a function from class B, not supposed to override'

	def funComm(self):
		print 'this is a simple func B'

a=A()
a.CallNoOverrideFun()
a.CallSimpleFun()

b=B()
b.CallNoOverrideFun()
b.CallSimpleFun()
