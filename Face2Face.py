# Given an unsorted array of size n. Array elements are in the range from 1 to n.
# One number from set {1, 2, …n} is missing and one number occurs twice in the array.
# Find these two numbers in order of one space.

inp = [5, 1, 2, 5, 3]


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def repeatMissing(arr):
    dup = 0
    miss = 0

    for i in range(len(arr)):
        while arr[i] != arr[arr[i] - 1]:
            swap(arr, i, arr[i] - 1)

    for i in range(len(arr)):
        if arr[i] != i+1:
            miss = i+1
            dup = arr[i]

    return miss, dup


print(repeatMissing(inp))
