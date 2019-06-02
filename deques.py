class Deque:
	
	def __init__(self):
		self.items = []
		
	def add_front(self, item):
		"""takes an item as a parameter and inserts at the 0th index of the list that is representing the deque."""
		"""Runtime is O(n) or linear time, because every time you insert an item at the 0th index or front of the list,
		all the other items in the list need to shift one position to the right."""
		self.items.insert(0, item)
	
	def add_rear(self, item):
		"""takes an item as a parameter and appends at the end of the list that is representing the deque."""
		"""Runtime is O(1) or constant time, because appending at the end of the list happens in constant time."""
		self.items.append(item)
	
	def remove_front(self):
		"""Removes and returns the item from the 0th index of the list, which represents the front of the deque."""
		"""Runtime is O(n) or linear time, because when we remove an item from the 0th index, all the other items
		have to shift one index to the left of the list."""
		if self.items:
			return self.items.pop(0)
		return None
	
	def remove_rear(self):
		"""Removes and returns the last item in the list which is representing the rear of the Deque."""
		"""Runtime is 0(1) or constant time, because all we're doing is indexing to the end of a list."""
		if self.items:
			return self.items.pop()
		return None
	
	def peek_front(self):
		"""Returns the value found at the 0th index of the list, which represents the front of the Deque."""
		"""Runtime is constant time or O(1), because all we're doing is indexing into a list."""
		if self.items:
			return self.items[0]
		return None
	
	def peek_rear(self):
		"""Returns the value found at the last index of the list, which represents the rear of the Deque."""
		"""Runtime is constant time or O(1), because all we're doing is indexing into a list."""
		if self.items:
			return self.items[-1]
		return None
	
	def size(self):
		"""Returns the length of the list representing the size of the Deque."""
		"""Runtime is O(1) or constant time, because all we are doing is finding the length of the list and
		returning that value."""
		return len(self.items)
	
	def is_empty(self):
		"""Checks to see if the list representing the Deque is empty. Returns True if it is, or False if it isn't."""
		"""Runtime is O(1) or constant time because all we're doing is comparing two values."""
		return self.items == []


my_deque = Deque()
print(my_deque.items)
print(my_deque.size())
print(my_deque.is_empty())
my_deque.add_front('apple')
print(my_deque.items)
my_deque.add_front('banana')
print(my_deque.items)
my_deque.add_rear('carrot')
print(my_deque.size())
print(my_deque.is_empty())
print(my_deque.items)
print(my_deque.peek_front())
print(my_deque.peek_rear())
my_deque.remove_front()
print(my_deque.items)
my_deque.remove_rear()
print(my_deque.items)

