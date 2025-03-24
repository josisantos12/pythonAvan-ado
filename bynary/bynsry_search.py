def binary_search(array, x, low, high):
    # Repete até que os ponteiros low e high se encontrem
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binary_search(array, x, 0, len(array)-1)