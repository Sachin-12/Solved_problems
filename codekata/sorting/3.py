# Q.No: 507

# You are an intern at GUVI and the company wants to organise its data and delete unnecessary extra storage elements used. You are given k arrays of unequal dimensions. Sort the k arrays individually and concatenate them.
 

# Input Description:
# First line contains the number of arrays. Subsequent lines contain the size of the array followed by the elements of the array.

# Output Description:
# An array containing the sorted elements of k sorted arrays

# Sample Input :
# 3
# 2
# 98 12
# 6
# 1 2 3 8 5 9
# 1
# 11

# Sample Output :
# 12 98 1 2 3 5 8 9 11



def store(arr,size,array_no):
    a = []
    for x in range(size):
        a.append(int(arr[x]))
    a.sort()
    return a

array_no = int(input())
arr =[]
array_size = 0
for x in range(array_no):
    array_md =[]
    array_size= array_size + int(input())
    a = input()
    array_md = a.split()
    array_md.sort()
    arr = arr + array_md

res = store(arr,array_size,array_no)
print(res)
   



