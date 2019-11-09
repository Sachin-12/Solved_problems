# # Pseudo code:
# get the text file path and read all the text
# create a dict and save every char and their count in that dict
# create a min heap from that dict

class HeapNode:
    def __init__(self,data,freq):
        self.data = data
        self.left = None
        self.right = None
        self.top = None
        self.freq = freq

loc = "sample.txt"
fp = open(loc,"r")
text = fp.read()
char_and_freq = dict()
count = 0

for ch in text:
    if ch in char_and_freq:
        i = char_and_freq[ch]
        char_and_freq[ch] = i+1 
    else:
        char_and_freq[ch] = 1

print(char_and_freq)
fp.close()

ArrayNode = []
i=0
for x in char_and_freq:
    ArrayNode.append(HeapNode)
    ArrayNode[i].data = x
    ArrayNode[i].freq = char_and_freq[x]
    i = i+1

for x in ArrayNode:
    print(x.freq)

def heapSort(char_and_freq):
    n = len(char_and_freq)


# def heapify(char_and_freq,n,i):

