
class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None

class Singly_Linked_List: 
 
	def __init__(self): 
		self.head = None

	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def deleteNode(self, position):

		temp1 = self.head 
		temp2 = self.head

		for i in range(position): 
			if temp2.next == None:
				if(i==position-1):
					self.head = self.head.next
				return self.head
			temp2 = temp2.next

		while(temp2.next != None):
			temp2 = temp2.next
			temp1 = temp1.next

		temp1.next = temp1.next.next

	def display_list(self): 
		temp = self.head 
		while(temp != None): 
			print(" {} ".format(temp.data)) 
			temp = temp.next

singly_linked_list = Singly_Linked_List() 
print("Press \"q\" to stop the list")
while(True):
	temp = input("Enter the number you want to add :")
	if temp == "q":
		break
	singly_linked_list.push(temp) 


print("Linked List :")
singly_linked_list.display_list() 
del_node = int(input("Enter the node you want to delete from the last in linked list"))
singly_linked_list.deleteNode(del_node) 
print("\nLinked List after deletion of {}th node from last: ".format(del_node))
singly_linked_list.display_list() 