class Stack:
	
	def __init__(self):
		self.items = []
		
	def push(self, item):
		"""Accepts an item as the parameter and appends it to the end of the list. Returns nothing."""
		"""The runtime for this method is O(1) or constant time because appending to the end of a list
		happens in constant time."""
		self.items.append(item)
	
	def pop(self):
		"""Removes and returns the last item from the list, which is also the top item of the stack"""
		"""The runtime here is constant time, because all it does is index to the last item of the list."""
		if self.items:
			return self.items.pop()
		return None
	
	def peek(self):
		"""This method returns the last item from the list, which is also the item at the top of the stack."""
		"""The runtime here is constant time, because all it does is index to the last item of the list"""
		if self.items:
			return self.items[-1]
		return None
	
	def size(self):
		"""This methods return the length of the list that is representing the stack."""
		"""This methods runs in constant time because finding the length of the list happens in constant time."""
		return len(self.items)
	
	def is_empty(self):
		"""This methods returns a boolean value describing whether or not the Stack is empty."""
		"""Testing of equality happens in constant time."""
		return self.items == []


stach_obj = Stack()
print(f"Is the stack empty?: {stach_obj.is_empty()}")
print(f"Size of the stack: {stach_obj.size()}")
stach_obj.push('apple')
print(stach_obj.items)
stach_obj.push('banana')
print(stach_obj.items)
stach_obj.push('carrot')
print(f"Is the stack empty?: {stach_obj.is_empty()}")
print(f"Size of the stack: {stach_obj.size()}")
print(stach_obj.items)
stach_obj.pop()
print(stach_obj.items)
stach_obj.pop()
print(stach_obj.items)
print('Next item to be removed')
print(stach_obj.peek())
print(f"Size of the stack: {stach_obj.size()}")
