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


# ar = [10, 3, 40, 20, 50, 80, 70]
# print(nearlySortedsearch(ar, 80, 0, len(ar)-1))


# Given a sorted array and a value x, the floor of x is the largest element in array smaller
# than or equal to x. Write efficient functions to find floor of x.


def floorElement(arr, ele):

    start = 0
    end = len(arr)-1
    res = None

    while start<=end:

        mid = (start+end)//2

        if arr[mid] <= ele:
            res = arr[mid]
            start = mid + 1

        elif arr[mid] > ele:
            end = mid-1

    return res


# print(floorElement([1, 2, 4, 8, 10, 10, 12, 19], 5))

def ceilElement(arr, ele):
    start = 0
    end = len(arr)-1
    res = None

    while start<=end:

        mid = (start+end)//2

        if arr[mid] >= ele:
            res = arr[mid]
            end = mid - 1

        elif arr[mid] < ele:
            start = mid + 1

    return res


arr = [1, 2, 8, 10, 10, 12, 19]

# print(ceilElement(arr, 10))


# Given an array of letters sorted in ascending order,
# find the smallest letter in the the array which is greater than a given key letter.


def alphaCeil(arr, alph):
    start = 0
    end = len(arr)-1

    res = None

    while start<=end:

        mid = (start+end)//2

        if arr[mid] > alph:
            res = arr[mid]
            end = mid-1

        else:
            start = mid + 1

    return res


aplhabets = ['a', 'c', 'f', 'h']
# print(alphaCeil(aplhabets, 'c'))

# find an element in an infinite array

def infiniteSearch(arr, ele):
    start = 0
    end  = 1

    while ele > arr[end]:
        start = end
        end = end * 2

    return binarySearch(arr, ele, start, end-1)


arr = [1, 2, 8, 10, 10, 12, 19]
# print(infiniteSearch(arr, 10))


# Given an infinite sorted array consisting 0s and 1s. The problem is to find the index of
# first ‘1’ in that array. As the array is infinite, therefore it is guaranteed that number
# ‘1’ will be present in the array.

def find1inBinary(arr):
    start = 0
    end = 1

    while 1>arr[end]:
        start = end
        end = end + end

    while start<=end:

        mid = (start+end)//2

        if arr[mid]>0 and arr[mid+1] == 1:
            return mid

        elif arr[mid] == arr[mid-1] == 1:
            end = mid - 1

        elif arr[mid] == 0:
            start = mid + 1

    return -1

# print(find1inBinary([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]))


# Given a sorted array, find the element in the array which
# has minimum difference with the given number.

def minDiff(arr, ele):
    bottom = floorElement(arr, ele)
    top = ceilElement(arr, ele)

    if abs(bottom-ele) > abs(top-ele):
        return top
    else:
        return bottom

# print(minDiff([1, 3, 8, 10, 13, 15], 12))


# A peak element is an element that is greater than its neighbors.

def findPeak(arr):
    low = 0
    high = len(arr)-1

    while low<=high:

        mid = (high+low)//2

        if mid>0 and mid <len(arr)-1:

            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid

            elif arr[mid - 1]> arr[mid]:
                high = mid-1

            else:
                low = mid+1

        elif mid==0:
            if arr[0] > arr[1]:
                return 0
            else:
                return 1

        elif mid == len(arr)-1:
            if arr[len(arr)-1] > arr[len(arr)-2]:
                return len(arr)-1
            else:
                return len(arr)-2
        else:
            return -1


# nums = [1,2,3,1]
nums = [1, 3, 4, 5, 6, 3, 2 ]
# print(findPeak(nums))


def bitonicarry(arr):
    left = findPeak(arr)
    right  = findPeak(arr[::-1])

    return left == (len(arr) - right-1)


nums = [1, 3, 5,  4, 5, 6, 3, 2 ]
# print(bitonicarry(nums))


# Given a bitonic sequence of n distinct elements, write a program to find a given element x
# in the bitonic sequence in O(log n) time. A Bitonic Sequence is a sequence of numbers which
# is first strictly increasing then after a point strictly decreasing.

def findinBiotonic(arr, ele):

    peak = findPeak(arr)
    left = binarySearch(arr, ele, 0, peak)
    right = binarySearch(arr, ele, peak, len(arr)-1)

    return max(left, right)


ar = [-3, 9, 8, 20, 17, 5, 1]
# print(findinBiotonic(ar, 20))



def searchMat(arr, ele):
    n = len(mat)
    m = len(mat[0])

    i =0
    j = len(mat[0]) - 1

    while i>=0 and i<n and j>=0 and j<m:
        if arr[i][j] == ele:
            return (i, j)

        elif arr[i][j] > ele:
            j -= 1

        elif arr[i][j] < ele:
            i += 1

    return -1


mat =  [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 45],
        [32, 33, 39, 50]]
# print(searchMat(mat, 29))


# Given number of pages in n different books and m students. The books are arranged
# in ascending order of number of pages. Every student is assigned to read some
# consecutive books. The task is to assign books in such a way that the maximum
# number of pages assigned to a student is minimum.

def isvalid(arr, n, pages, key):
    students = 1
    sum = 0
    for i in arr:
        sum += i
        if sum>pages:
            students+=1
            sum = i

    if students>key:
        return False

    return True

def allocatePage(arr, key):
    n =len(arr)
    start = max(arr)
    end = sum(arr)
    result = -1
    temp_arr = list(range(start, end+1))

    if n<key:
        return -1

    while start<=end:
        mid = (start+end)//2

        if isvalid(arr, n, mid, key):
            result = mid
            end = mid-1

        else:
            start = mid+1

    return result




ar = [12, 34, 67, 90]
m = 2

# print(allocatePage(ar, m))





















