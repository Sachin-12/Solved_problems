T = [7,4,5,1,9,2,6,3]
res=[]
for i in range(len(T)):
    f=0
    for j in range(i+1,len(T)-1):
        if T[i]<T[j]:
            f=j-i
            break
    if f==0:
        res.append(f)
    else:
        res.append(f)

print(res)

