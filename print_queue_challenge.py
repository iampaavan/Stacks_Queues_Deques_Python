import random


class Queue:
	
	def __init__(self):
		self.items = []
		
	def enqueue(self, item):
		self.items.insert(0, item)
		
	def dequeue(self):
		if self.items:
			return self.items.pop()
		return None
	
	def is_empty(self):
		return self.items == []
	

class Job:
	
	def __init__(self):
		self.pages = random.randint(1, 11)
		
	def print_page(self):
		if self.pages > 0:
			self.pages -= 1
			
	def check_complete(self):
		if self.pages == 0:
			return True
		return False
	
	
class Printer:
	
	def __init__(self):
		self.current_job = None
		
	def get_job(self, print_queue):
		try:
			self.current_job = print_queue.dequeue()
		except IndexError:
			return f"No Jobs to Print."
		
	def print_job(self, job):
		while job.pages > 0:
			job.print_page()
			
		if job.check_complete():
			return f"Printing Complete."
		
		else:
			return f"An error occurred."


my_queue = Queue()
my_job = Job()
my_printer = Printer()

my_queue.enqueue('job_1')
print(my_queue.items)
my_queue.enqueue('job_2')
my_queue.enqueue('job_3')
print(my_queue.items)

my_printer.get_job(my_queue)
print(my_printer.print_job(my_job))

