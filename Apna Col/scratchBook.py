def pivot(arr, low, high):
    if low >= high:
        return

    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]

    i = low
    while i < high:
        if arr[i] <= arr[high]:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
        i += 1

    arr[low], arr[high] = arr[high], arr[low]
    return low


def QuickSort(arr, low, high):
    if low >= high:
        return

    piv = pivot(arr, low, high)
    QuickSort(arr, low, piv-1)
    QuickSort(arr, piv+1, high)


Arr = [5, 3, 9, 6, 4, 7, 5, 2, 8, 9, 4, 12, 2, 9, 5, 6, 8, 4, 5, 3, 6, 9, 5, 2, 3, 6, 4]
print(QuickSort(Arr, 0, len(Arr) - 1))
print(Arr)

