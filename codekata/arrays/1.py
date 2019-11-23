# Q.No 644 // Successful output
# You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result
# 
# Input Description:
# You are given a long string of digits
# 
# Output Description:
# Print the desired result print -1 if result length is 0
# 
# Sample Input :
# 1331
# 
# Sample Output :
# -1


num = int(input())
a =[]
def count_digits(num):
    count = 0
    while num > 0:
        count= count+1
        num = num //10
    return count

def num_arr(num,count):
    for i in range(count):
        a.append(num % 10)
        num = num //10
    a.reverse()

def remove_duplicates(num,digits):
    i=0  
    try: 
        while(a[i+1]):
            if (a[i]==a[i+1]):
                del(a[i])
                del(a[i])
                i=1-1
                continue
            i=i+1
    except IndexError:
        pass 
    return len(a)           

digits = count_digits(num)
num_arr(num,digits)
arr_size = remove_duplicates(num,digits)
if arr_size == 0:
    print("-1")
else:
    listToStr = ''.join([str(x) for x in a ])
    print(listToStr)