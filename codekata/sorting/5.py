# Q.No: 699 (success)

# You are given a number ‘n’. Your task is to create the smallest number possible using the digits of number.

# Input Description:
# You are given a number ‘n’,

# Output Description:
# Print the smallest possible number of same length

# Sample Input :
# 123456789123456789

# Sample Output :
# 112233445566778899
def mergesort(a):
    if len(a)>1:
        mid = len(a)//2
        l= a[:mid]
        r= a[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        
        while i <len(l):
            a[k] =l[i]
            i+=1
            k+=1

        while j < len(r):

            a[k]= r[j]
            j+=1
            k+=1


n = input()
size = len(n)
a=[]
for x in range(size):
    a.append(int(n[x]))
mergesort(a)

def smallest(a):
    for i,n in enumerate(a):
        if n != 0:
            tmp = a.pop(i)
            break
    a.insert(0,tmp)

smallest(a)

for i in range(size):
    print(a[i],end="")