class Deque:
	
	def __init__(self):
		self.items = []
		
	def add_front(self, item):
		self.items.insert(0, item)
		
	def add_rear(self, item):
		self.items.append(item)
		
	def remove_front(self):
		return self.items.pop(0)
	
	def remove_rear(self):
		return self.items.pop()
	
	def size(self):
		return len(self.items)
	
	
def check_palindrome(input_string):
	
	my_d = Deque()
	
	for character in input_string:
		my_d.add_rear(character)
		
	while my_d.size() >= 2: # Size 0 or 1 depicts the string is a palindrome.
		
		front_item = my_d.remove_front()
		rear_item = my_d.remove_rear()
		
		if front_item != rear_item:
			return False
		
	return True


print(check_palindrome('racecar'))
print(check_palindrome('kayak'))
print(check_palindrome('oranges'))
print(check_palindrome(''))
print(check_palindrome('a'))
