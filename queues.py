class Queue:

	def __init__(self):
		'''Initialize the list to an empty list.'''
		self.items = []
		
	def enqueue(self, item):
		"""Takes in an item and inserts that item into the 0th index of the list that is representing the Queue."""
		"""Runtime is O(n) or linear time, because inserting at the 0th index of a list forces all the other items
		in the list to move one index to the right."""
		self.items.insert(0, item)
	
	def dequeue(self):
		"""Returns and removes the front-most item of the Queue, which is represented by the last item in the list."""
		"""Runtime is O(1) or constant time, because indexing to the end of a list happens in constant time"""
		if self.items:
			return self.items.pop()
		return None
	
	def peek(self):
		"""Returns the last item in the list, which represents the front-most item in the Queue."""
		"""The runtime is O(1) or constant time, because we're just indexing to the last item of the List
		and returning the value found there."""
		if self.items:
			return self.items[-1]
		return None
	
	def size(self):
		"""Returns the size of the Queue, which is represented by the length of the list."""
		"""Runtime is O(1) or constant time, because we're only returning the length of the list"""
		return len(self.items)
	
	def is_empty(self):
		"""Returns a boolean value expressing whether or not the list representing the Queue is empty."""
		"""Runtime is O(1) or constant time, because it's only checking the equality."""
		return self.items == []
	

my_queue = Queue()
my_queue.enqueue('apple')
print(my_queue.items)
my_queue.enqueue('banana')
print(my_queue.items)
my_queue.dequeue()
print(my_queue.items)
my_queue.enqueue('apple')
print(my_queue.items)
print(my_queue.peek())
print(my_queue.size())
print(my_queue.is_empty())


