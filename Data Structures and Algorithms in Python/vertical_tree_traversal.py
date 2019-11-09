class Node:  
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None

def getVerticalOrder(root, hd, m): 
	if root is None: 
		return
	try: 
		m[hd].append(root.key) 
	except: 
		m[hd] = [root.key]
	getVerticalOrder(root.left, hd-1, m) 
	getVerticalOrder(root.right, hd+1, m) 

def printVerticalOrder(root): 
	m = dict() 
	hd = 0
	getVerticalOrder(root, hd, m)
	for index, value in enumerate(sorted(m)): 
		for i in m[value]: 
			print(i)


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 
print("Vertical order traversal is")
printVerticalOrder(root) 
