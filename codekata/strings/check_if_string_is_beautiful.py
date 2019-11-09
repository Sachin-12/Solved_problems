# You are given a string ‘s’. Your task is to tell whether string is 
# beautiful or not.A beautiful string is a string in which String starts 
# with ‘a’ or ‘A’ and middle element is either ‘m’ or ‘M’ and last element is ‘z’or ‘Z’


# Input Description:
# You are given a string ‘s’.

# Output Description:
# Print 1 if string is beautiful and 0 if it is not

# Sample Input :
# Amz

# Sample Output :
# 1


s = input()

def check_string_beauty(s):

    start = 0
    end = len(s)
    mid = (start+end)//2
    flag = 0

    if (s[start] == "a" or s[start] == "A"):
        if (s[end-1] == "z" or s[end-1] == "Z"):
            if (s[mid] == "m" or s[mid] == "M"):
                flag = 1
                return flag
    
    return flag

result = check_string_beauty(s)
if result == 0:
    print("0")
else:
    print("1")
            
