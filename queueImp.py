#size dequeue enqueue isEmpty init Queue is FIFO

class Queue:
	def __init__(self):
		self.items = []

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		# pop take out last element - FIFO
		return self.items.pop()
		

def main():
	q = Queue()
	print 'empty queue'

	print 'size 0'
	print q.size()

	print 'should return empty'
	print q.isEmpty()
	
	#print q.dequeue()

	print 'added hello'
	print q.enqueue('hello')

	print 'size 1'
	print q.size()

	print 'added 10'
	print q.enqueue(10)

	print 'size 2'
	print q.size()

	print q.dequeue()

	print 'size 1'
	print q.size()

	print 'should return false'
	print q.isEmpty()

	print 'size 1'
	print q.size()
	print q.enqueue(40)

	print q

	print 'final size 2'
	print q.size()

	print 'not empty'
	print q.isEmpty()


if __name__ == '__main__':
	main()

