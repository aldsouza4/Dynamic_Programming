def countcanjump(arr, i=0):
    if i >= len(arr):
        return False

    elif i == len(arr) - 1:
        return True

    for k in range(1, arr[i] + 1):
        if countcanjump(arr, i + k):
            return True

    return False


print(countcanjump([2, 3, 1, 1, 4]))