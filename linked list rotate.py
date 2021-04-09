class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None
		self.count = 0

	def insert(self,new_data):
		new_node = node(new_data)
		new_node.next = self.head
		self.head = new_node
		self.count += 1

	def append_array(self,array):
		for i in array:
			self.insert(i)

	def rotate(self):
		old_head = self.head.data
		lst = linked_list()
		while self.head.next != None:
			lst.insert(self.head.next.data)
			self.head = self.head.next
		lst.append_array([old_head])
		lst.print()
		return lst
		
	def print(self):
		temp = self.head
		temp_list =[]
		while (temp):
			temp_list.append(temp.data)
			temp = temp.next
		print(temp_list)


llist = linked_list()
array =[1,2,3,4,5]

llist.append_array(array)

llist.rotate()