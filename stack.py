
class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node


class Stack:
	def __init__(self):
		self.top = None
	
	def peek(self):
		return self.top
	
	def push(self, data):
		node = self.top
		self.top = Node(data)
		self.top.next_node = node

	def pop(self):
		if self.top is None:
			return None
		node = self.top
		self.top = self.top.next_node
		return node
