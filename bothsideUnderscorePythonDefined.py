# __xyz__ is an python defined function, you can override that func as well
number = 10
print number.__add__(2)
# here + is calling python defined __add__ func
print number + 1

class FalseCalculator(object):

	def __init__(self, number1):
		self.number = number1

	def __add__(self, number2):
		return self.number - number2


fc = FalseCalculator(10)
print fc.__add__(1)








