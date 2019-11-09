import sys
sys.setrecursionlimit(5000)

class MinHeapNode:
    def __init__(self,data,freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

class MinHeap:
    def __init__(self,size,capacity,MinHeapNode):
        self.size = size
        self.capacity = capacity
        self.array_mhn = MinHeapNode

def newNode(data,freq):
    temp = MinHeapNode
    temp.left = None
    temp.right = None
    temp.freq = freq
    temp.data = data
    return temp

def createMinHeap(capacity):
    minHeap = MinHeap

    # extra line
    minHeap.array_mhn = []
    minHeap.size = 0
    minHeap.capacity = capacity
    return minHeap

def minHeapify(minHeap,i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if(l < minHeap.size and minHeap.array_mhn[l].freq < minHeap.array_mhn[smallest].freq):
        smallest = l
    if(r < minHeap.size and minHeap.array_mhn[r].freq < minHeap.array_mhn[smallest].freq):
        smallest = r

    if smallest != i:
        minHeap.array_mhn[smallest],minHeap.array_mhn[i] = minHeap.array_mhn[i],minHeap.array_mhn[smallest]

def isSizeOne(minHeap):
    return minHeap.size == 1

def extractMin(minHeap):
    temp = minHeap.array_mhn[0]
    minHeap.array_mhn[0] = minHeap.array_mhn[minHeap.size-1]
    minHeap.size = minHeap.size-1
    minHeapify(minHeap,0)
    return temp

def insertMinHeap(minHeap, minHeapNode):
    minHeap.size = minHeap.size + 1
    i = minHeap.size - 1
    while(i and minHeapNode.freq < minHeap.array_mhn[(i-1)//2].freq):
        i = (i-1)//2
    minHeap.array_mhn[i] = minHeapNode

def buildMinHeap(minHeap):
    n = minHeap.size - 1
    for i in range ((n-1)//2,-1,-1):
        minHeapify(minHeap,i)

def printArr(arr,n):
    for i in range(n):
        print(arr[i])

def isLeaf(root):
    return not root.left and not root.right

def createAndBuildMinHeap(data,freq,size):
    minHeap = createMinHeap(size)
    for i in range (size):
        minHeap.array_mhn.append(newNode(data[i],freq[i]))
    minHeap.size = size
    buildMinHeap(minHeap)
    return minHeap

def buildHuffmanTree(data,freq,size):
    left = MinHeapNode
    right = MinHeapNode
    top = MinHeapNode
    minHeap = createAndBuildMinHeap(data,freq,size)
    while(not isSizeOne(minHeap)):
        left = extractMin(minHeap)
        right = extractMin(minHeap)
        top = newNode(None,left.freq + right.freq)
        top.left = left
        top.right = right
        insertMinHeap(minHeap,top)
    return extractMin(minHeap)

def printCodes(root,arr,top):
    if root.left:
        arr.append(0)
        printCodes(root.left,arr,top+1)
    if root.right:
        arr.append(1)
        printCodes(root.right,arr,top+1)
    if isLeaf(root):
        print(root.data)
        printArr(arr,top)

def HuffmanCodes(data,freq,size):
    root = buildHuffmanTree(data,freq,size)
    arr = []
    top = 0
    printCodes(root,arr,top)

arr = ['a','b','c','d','e','f']
freq = [5,9,12,13,16,45]
size = len(arr)//len(arr[0])
HuffmanCodes(arr,freq,size)