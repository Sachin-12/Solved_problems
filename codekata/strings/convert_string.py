# Write a program to get a string S, Type of conversion 
# (1 - Convert to Lowercase, 2 - Convert to Uppercase) T, and integer P . 
# Convert the case of the letters in the positions which are multiples of P.(1 based indexing).

# Input Description:
# Given a string S, Type of conversion T, and integer P

# Output Description:
# Convert the case of the letters and print the string

# Sample Input :
# ProFiLe
# 1
# 2

# Sample Output :
# Profile

import sys

S = input()
T = int(input())
P = int(input())

if P > len(S)-1:
    print("Invalid  Index")
    sys.exit()

def convert_string(s,t,indices):
    l = len(s)
    new_string = ""
    if t == 1:
        new_string = ("".join(x.lower() if i in indices else x for i,x in enumerate(s)))
    elif t == 2:
        new_string = ("".join(x.upper() if i in indices else x for i,x in enumerate(s)))
    else:
        return 0
    return new_string

def indices_to_be_converted(s,p):
    l = len(s) 
    indexes =[]
    for i in range(p-1,l,p):
        indexes.append(i)
    return indexes

indices = indices_to_be_converted(S,P)
result = convert_string(S,T,indices)
print(result) if result else print("Invalid Type")