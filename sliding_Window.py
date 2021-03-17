# maximum contiguious subarray sum

def sldingwindow(arr, window):
    mx = -1 * float('inf')
    for i in range(len(arr) - window + 1):
        temp = sum(arr[i:i + window + 1])

        mx = max(mx, temp)

    return mx


def max_sum(arr):
    mx1 = -1 * float('inf')

    for j in range(1, len(arr)):
        temp = sldingwindow(arr, j)

        mx1 = max(mx1, temp)

    return mx1


ar = [4, 1, 1, 1, 2, 3, 5]


# print(max_sum(ar))


def slidingij(arr, win):
    i = 0
    j = 0
    mx = -1 * float('inf')
    temp_sum = 0

    while j < len(arr):
        temp_sum += arr[j]

        if (j - i + 1) < win:
            j += 1

        elif j - i + 1 == win:
            mx = max(mx, temp_sum)
            temp_sum -= arr[i]
            i += 1
            j += 1

    return mx


# vector = [12, -1, -7, 8, -15, 30, 16, 28]

# ar = [4, -1, 1, 1, -2, 3, -5, 4, -1, 1]

# print(sldingwindow(ar, len(ar)))
# print(slidingij(ar, len(ar)))

# print(slidingij(ar, 3))

# Given an array and a positive integer k, find the first negative integer for
# each and every window(contiguous subarray) of size k.

def negative_window(arr, win):
    i = 0
    j = 0
    neglist = []
    resultList = []

    while j < len(arr):

        if arr[j] < 0:
            neglist.append(arr[j])

        if j - i + 1 < win:
            j += 1

        elif j - i + 1 == win:
            if len(neglist) == 0:
                resultList.append(0)

            else:
                resultList.append(neglist[0])

            if len(neglist) > 0 and arr[i] == neglist[0]:
                neglist = neglist[1:]

            i += 1
            j += 1

    return resultList


# print(negative_window(vector, 3))

def check_anagram(large_str, check_str):
    k = len(check_str)

    map = {}

    for i in check_str:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1

    i = 0
    j = 0
    count = len(map)
    ans = 0

    while j < len(large_str):
        if large_str[j] in map:
            map[large_str[j]] -= 1

        if map.get(large_str[j]) == 0:
            count -= 1

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:

            if count == 0:
                ans += 1

            if large_str[i] in map:
                map[large_str[i]] += 1

                if map.get(large_str[i]) == 1:
                    count += 1

            i += 1
            j += 1

    return ans


# print(check_anagram("ABCHJTABCCBAABCDHDJSJ", "ABC"))

def maxWindow(arr, win):
    i = 0
    j = 0
    list_max = []
    ele_max = -1 * float('inf')

    while j < len(arr):

        if arr[j] > ele_max:
            ele_max = arr[j]

        if j - i + 1 < win:
            j += 1

        elif j - i + 1 == win:

            list_max.append(ele_max)
            if j < len(arr) - 1 and arr[j + 1] > ele_max:
                ele_max = arr[j + 1]

            i += 1
            j += 1

    return list_max


# print(maxWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))


# Given an array containing N positive integers and an integer K. Your task is to
# find the length of the longest Sub-Array with sum of the elements equal to the
# given value K.

def sldingwindowsize(arr, window, k):
    mx = -1 * float('inf')
    for i in range(len(arr) - window + 1):
        temp = sum(arr[i:i + window + 1])
        if temp == k:
            mx = max(mx, len(arr[i:i + window + 1]))

    return mx


def max_sumsize(arr, k):
    mx1 = -1 * float('inf')

    for j in range(1, len(arr)):
        temp = sldingwindowsize(arr, j, k)

        mx1 = max(mx1, temp)

    return mx1


# v = [4, 1, 1, 1, 2, 3, 5]
# k = 5
# print(max_sumsize(v, 5))


def maxSizesum(arr, k):
    i = 0
    j = 1

    mx = 0

    while j < len(arr):
        temp = sum(arr[i:j])

        if temp == k:
            mx = max(mx, len(arr[i:j]))

        elif temp > k:
            while temp > k:
                temp -= arr[i]
                i += 1

        j += 1

    return mx


# v = [4, 1, 1, 1, 2, 3, 5]
# k = 5
# print(maxSizesum(v, k))


