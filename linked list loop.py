class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None

	def insert(self,new_data):
		new_node = node(new_data)
		new_node.next = self.head
		self.head = new_node


	def detect_loop(self):
		set1 = set()
		temp = self.head
		while (temp):
			if (temp in set1):
				return True
			set1.add(temp)
			temp = temp.next
		return False

#Driver cod efor testing
llist = linked_list()
llist.insert(20)
llist.insert(4)
llist.insert(15)
llist.insert(10)

#creating a loop for testing
llist.head.next.next.next.next = llist.head


if (llist.detect_loop()):
	print('loop_found')
else:
	print('loop_not_found')

