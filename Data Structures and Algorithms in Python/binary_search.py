def binary_search(sorted_list, elem):
    start = 0
    end = len(sorted_list)
    while start < end:
        mid = (start + end)//2
        if sorted_list[mid] > elem:
            end = mid
        elif sorted_list[mid] < elem:
            start = mid + 1
        else:
            return mid
    return -1
 
 
unsorted_list = input('Enter the unsorted list of numbers: ')
unsorted_list = unsorted_list.split()
unsorted_list = [int(x) for x in unsorted_list]
elem = int(input('Enter the number to search for: '))
 
unsorted_list.sort()
position = binary_search(unsorted_list,elem)
if position < 0:
    print('{} was not found.'.format(elem))
else:
    print('{} was found at position {}.'.format(elem, position))