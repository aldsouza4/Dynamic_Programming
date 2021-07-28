# A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
# A2[] = {2, 1, 8, 3}


def relativeSort(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1


    for i in arr2:
        for j in arr2:
