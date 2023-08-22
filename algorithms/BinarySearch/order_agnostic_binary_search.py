"""
Find a index of an element in a given list

The given input array is sorted but don't know whether it is ascending or descending

************

Time Complexity:

if target == mid_element then time_complexity is O(n)
else in other cases we are looping through an array and divide it and find an element.
So, the time_complexity is O(log n).


"""

def is_ascending(input_list):
    if input_list[0] < input_list[len(input_list) - 1]:
        return True

    return False

def perform_ascending_search(input_list, target, start, end):
    while start <= end:
        mid = round((start + end) / 2)
        mid_element = input_list[mid]

        if target == mid_element:
            return mid

        if target < mid_element:
            end = mid - 1
        elif target > mid_element:
            start = mid + 1
    
    return -1

def perform_descending_search(input_list, target, start, end):
    while start <= end:
        mid = round((start + end) / 2)
        mid_element = input_list[mid]

        if target == mid_element:
            return mid

        if target > mid_element:
            end = mid - 1
        elif target < mid_element:
            start = mid + 1
    
    return -1

def binary_search(input_list, target):

    ascending = is_ascending(input_list=input_list)
    start = 0
    end = len(input_list) - 1

    if ascending:
        return perform_ascending_search(
            input_list=input_list, 
            target=target, 
            start=start, 
            end=end
        )

    return perform_descending_search(
            input_list=input_list,
            target=target,
            start=start,
            end=end
        )


if __name__ == "__main__":
    
    input_list = [1,3,5,6,10,12,15,20,21,28]
    target = 28
    binary_search_ouput = binary_search(input_list, target)

    print(binary_search_ouput)

    input_list = [25,22,18,15,13,10,9,7,5,3]
    target = 4
    binary_search_ouput = binary_search(input_list, target)

    print(binary_search_ouput)