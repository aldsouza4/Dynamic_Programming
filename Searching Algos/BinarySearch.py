def binarySearch(arr, element, start, end):
    if end >= start:
        mid = (start + end) // 2

        if arr[mid] == element:
            return mid

        elif arr[mid] < element:
            start = mid + 1
            return binarySearch(arr, element, start, end)

        elif arr[mid] > element:
            end = mid - 1
            return binarySearch(arr, element, start, end)
    else:
        return -1


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(x) - 1

print(binarySearch(x, 2, 0, n))