# Given an unsorted array of size n. Array elements are in the range from 1 to n.
# One number from set {1, 2, …n} is missing and one number occurs twice in the array.
# Find these two numbers in order of one space.

inp = [3, 1, 2, 5, 3]


def duprepetCheck(arr):
    missing = None
    duplicate = None

    for i in range(len(arr)):
        if arr[i] != arr[arr[i] - 1]:
            arr[i], arr[arr[i] - 1] = arr[arr[i] - 1], arr[i]

    return arr


print(duprepetCheck(inp))
