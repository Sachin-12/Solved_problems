def delete_root(max_heap,n):
    last_elem = max_heap[n-1]
    max_heap[0] = last_elem
    n = n-1
    max_heap.pop()
    heapify(max_heap,n,0)
    print_max_heap(max_heap,n)

def heapify(max_heap,n,i):
    largest = i
    left = (2*i)+1
    right = (2*i)+2

    if(left < n and max_heap[left]> max_heap[largest]):
        largest = left
    if(right < n and max_heap[right]> max_heap[largest]):
        largest = right

    if(largest != i):
        (max_heap[i],max_heap[largest]) = (max_heap[largest],max_heap[i])
        print(max_heap)
        heapify(max_heap,n,largest)

def print_max_heap(max_heap,n):
    for i in range (n):
        print(max_heap[i])


max_heap = [12,10,8,6,7,3,4]
n = len(max_heap)
delete_root(max_heap,n)

