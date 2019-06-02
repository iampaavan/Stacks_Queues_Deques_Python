class Stack():
	
	def __init__(self):
		self.items = []
		
	def is_empty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
	
	
s = Stack()
string = input(f"Enter the string:")
rev_string = ''

for character in string:
	s.push(character)

while not s.is_empty():
	rev_string += s.pop()
	
if string == rev_string:
	print(f"Given string is a palindrome.")
	
else:
	print(f'The string is not a palindrome.')

