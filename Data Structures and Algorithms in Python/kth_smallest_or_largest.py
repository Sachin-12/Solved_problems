def find_smallest(array,k):
    return array[k-1]

def find_largest(array,k):
    return array[len(array)-k]

array = input("Enter the array :")
k = int(input("Enter the Kth smallest and largest element to be found :"))

array = array.split()
array =[int(x) for x in array]
array.sort()
smallest = find_smallest(array,k)
largest = find_largest(array,k)

print("The {}th Smallest element in the array is {} ".format(k,smallest))
print("The {}th Largest element in the array is {} ".format(k,largest))



