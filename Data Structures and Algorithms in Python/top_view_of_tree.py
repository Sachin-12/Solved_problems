class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0

def topView(root):
    if root == None:
        return
    q =[]
    hd =0
    root.hd = hd
    m = dict()

    q.append(root)

    while(len(q)):
        root = q[0]
        hd = root.hd

        if hd not in m:
            m[hd]= root.data
        if(root.left):
            root.left.hd = hd-1
            q.append(root.left)
        if (root.right):
            root.right.hd = hd+1
            q.append(root.right)
        q.pop(0)

    print(m)
    
    for i in sorted(m):
        print(m[i],end="")

       
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
topView(root)