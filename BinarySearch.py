def binarySearch(arr, element, start, end):
    if end >=start:
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
# print(binarySearch(x, 4, 0, n))
x.reverse()


# Find in reverse sorted array

def revbinarySearch(arr, element, start, end):
    if end >= start:
        mid = (start + end) // 2

        if arr[mid] == element:
            return mid

        elif arr[mid] < element:
            end = mid - 1
            return revbinarySearch(arr, element, start, end)

        elif arr[mid] > element:
            start = mid + 1
            return revbinarySearch(arr, element, start, end)
    else:
        return -1


# print(revbinarySearch(x, 4, 0, n))

def dunnoOredrsearch(arr, ele):
    if len(arr) == 1:
        if arr[0] == ele:
            return True
        else:
            return False

    n = len(arr) - 1

    if arr[0] < arr[1]:
        return binarySearch(arr, ele, 0, n)
    else:
        return revbinarySearch(arr, ele, 0, n)


# print(dunnoOredrsearch(x, 4))

x = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10]


def findOccurances(arr, ele):
    start = 0
    end = len(arr) - 1

    def binarySearch_left(arr, element, start, end):
        res_l = 0

        while end >= start:

            mid = (start + end) // 2

            if arr[mid] == element:
                res_l = mid
                end = mid-1

            elif arr[mid] < element:
                start = mid+1

            else:
                end = mid -1

        return res_l

    def binarySearch_right(arr, element, start, end):
        res_r = 0

        while end >= start:

            mid = (start + end) // 2

            if arr[mid] == element:
                res_r = mid
                start = mid+1

            elif arr[mid] < element:
                start = mid+1

            else:
                end = mid -1

        return res_r


    return binarySearch_right(arr, ele, start, end) - binarySearch_left(arr, ele, start, end) + 1


# print(findOccurances(x, 4))

# Find the Rotation Count in Rotated Sorted array
# Consider an array of distinct numbers sorted in increasing order. The array
# has been rotated (clockwise) k number of times. Given such an array, find the value of k.

def findRotations(arr):
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start+end)//2
        prev = (mid + n -1)%n
        nxt = (mid + 1)%n

        if arr[prev] > arr[mid] and arr[nxt] > arr[mid]:
            return mid

        elif arr[mid] <= arr[end]:
            end = mid - 1

        elif arr[start] <= arr[mid]:
            start = mid+1

    return -1


ar = [15, 18, 2, 3, 6, 12]
# print(findRotations(ar))


# FIND AN ELEMENT IN A ROTATED SORTED ARRAY:

def findinRotated(arr, ele):

    ind = findRotations(arr)

    return max(binarySearch(arr, ele, 0, ind-1), binarySearch(arr, ele, ind, len(arr)-1))


# print(findinRotated(ar, 3))

# Given an array which is sorted, but after sorting some elements are moved to either of the adjacent
# positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search
# an element in this array. Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].

def nearlySortedsearch(arr, element, start, end):

    while end >= start:

        mid = (start + end) // 2

        if arr[mid] == element:
            return mid

        elif (mid-1)>=start and arr[mid-1] == element:
            return mid-1

        elif (mid+1)>=start and arr[mid+1] == element:
            return mid+1

        elif arr[mid] < element:
            start = mid+2

        else:
            end = mid - 2

    return -1


ar = [10, 3, 40, 20, 50, 80, 70]
# print(nearlySortedsearch(ar, 80, 0, len(ar)-1))

