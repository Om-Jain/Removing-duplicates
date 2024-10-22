def remove_duplicates(arr):
    if not arr:
        return 0
    
    unique_index = 0
    
    # Iterate through the array with the fast pointer
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]
    
    # Return the number of unique elements
    return unique_index + 1

arr = [1, 1, 2, 2, 2, 3, 3]
k = remove_duplicates(arr)
print(f"Array after removing duplicates: {arr[:k]}")
