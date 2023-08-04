# This is a simple algorithm in python that searches for an element in an array

arr = [1, 3, 3, 4, 5, 6, 7, 8, 9]


# Python implementation of Binary Search
def binarySearch(arr, target):
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid
    return -1
