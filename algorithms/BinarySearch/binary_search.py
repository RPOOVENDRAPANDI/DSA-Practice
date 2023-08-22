"""
Find a index of an element in a given list

1,3,5,6,10,12,15,20,21,28 => Ascending

Find the index of an element 12

*************

To implement a binary search the list or an array must be sorted either in ascending or descending

"""

def binary_search(input_list, target):
    """
    Binary search to find an element in a given list
    """
    
    # Finding start, mid and end for a given list
    start = 0
    end = len(input_list) - 1
    
    while start <= end: # The only situation when start is greater than the end is when we completely loop through all the elements in an array
        mid = round((start + end) / 2)

        if target == input_list[mid]:
            return mid
        
        if target > input_list[mid]: # Focus on right side
            start = mid + 1
        elif target < input_list[mid]: # Focus on Left side
            end = mid - 1
    
    return -1



if __name__ == "__main__":

    input_list = [1,3,5,6,10,12,15,20,21,28]
    target = 28
    binary_search_ouput = binary_search(input_list, target)

    print(binary_search_ouput)