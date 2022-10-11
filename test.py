class Node:
		
	def __init__(self,value=None):
		self.value = value
		self.next = None

	def __str__(self):
		return f"{self.value} -> {self.next}"

class SLinkedList:

	def __init__(self):
		self.head = None

	def push(self,v):
		n = Node(v)
		n.next = self.head
		self.head = n

	def push_end(self,v):
		n = Node(v)
		if self.head is None:
			self.head = n
			return
		last = self.head
		while(last.next):
			last = last.next
		last.next=n

	def get_list(self):
		table=[]
		value = self.head
		while value is not None:
			table.append(value.value)
			value = value.next
		return table

	def print_list(self):
		return str(self.head).split(" -> ")

	def print_last(self):
		return str(self.dernier)

	def __str__(self) :
		return str(self.head)

list = SLinkedList()

list.push("Kingson")
list.push("Eddie")
list.push("Edouard")

list.push_end("Jon")

print() # empty line

print(list)

print() # empty line

m = list.get_list()

print(*m,sep="\n")

print() # empty line

for k,v in enumerate(m):
	print(k,v)

print() # empty line
