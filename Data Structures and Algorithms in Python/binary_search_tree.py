numbers = [12,22,88,90,3,35,1,8,200]

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def insert(root,new_node):
    if root is None:
        root = new_node
    else:
        if root.data < new_node.data:
            if root.right is None:
                root.right = new_node
            else:
                insert(root.right,new_node)

        else:
            if root.left is None:
                root.left = new_node
            else:
                insert(root.left,new_node)
def search(root,key):
    if root is None or root.data == key:
        return root
    
    if root.data < key:
        return search(root.right,key)
    
    return search(root.left,key)

def display_tree(root):
    if root:
        display_tree(root.left)
        print(root.data)
        display_tree(root.right)

r = Node(50)

insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))


value= (search(r,70))
print(value.data)

display_tree(r)
