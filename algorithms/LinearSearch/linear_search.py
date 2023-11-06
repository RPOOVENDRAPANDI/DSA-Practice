"""
Consider the array arr[] = {10, 50, 30, 70, 80, 20, 90, 40} and key = 30

Need to return the index of an key present in the array
"""

def linear_search(input_values, key):

    for i in range(0, len(input_values)):
        if input_values[i] == key:
            return i

    return -1


if __name__ == "__main__":
    input_array = [10, 50, 30, 70, 80, 20, 90, 40]
    key = 30

    linear_search_output = linear_search(input_values=input_array, key=key)
    
    if linear_search_output == -1:
        print("No Match Found!!!")
    else:
        print(f"The index of key {key} is {linear_search_output}")