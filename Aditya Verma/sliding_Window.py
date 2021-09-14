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


# ar = [4, 1, 1, 1, 2, 3, 5]

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
# Given a word pat and a text txt. Return the count of the occurrences of
# anagrams of the word in the text.

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

# Given an array arr[] of size N and an integer K. Find the maximum for
# each and every contiguous subarray of size K.

def max_of_subarrays(arr, n, k):
    if k == 1:
        return arr

    if k > n:
        return max(arr)

    i, j = 0, 0
    ans = []
    quque = []

    while j < n:

        if j - i < k:
            while quque and quque[-1] < arr[j]:
                quque.pop()
            quque.append(arr[j])

        if j - i + 1 == k:
            ans.append(quque[0])

            if quque[0] == arr[i]:
                quque.pop(0)

            i += 1

        j += 1

    return ans


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
# Given an array containing N positive integers and an integer K. Your task is to find the
# length of the longest Sub-Array with sum of the elements equal to the given value K.

def maxSizesum(arr, k):
    i = 0
    j = 0

    mx = 0
    temp = 0

    while j < len(arr):
        temp += arr[j]

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

v = ["a", "a", "b", "a", "c", "b", "e", "b", "e", "b", "e"]


# Given a string you need to print the size of the longest possible
# substring that has exactly k unique characters.

def largestuniquestr(arr, k):
    i = 0
    j = 0
    mx = 0
    map = {}

    while j < len(arr):

        if arr[j] in map:
            map[arr[j]] += 1

        elif arr[j] not in map:
            map[arr[j]] = 1

        if len(map) == k:
            mx = max(mx, sum(map.values()))

        elif len(map) > k:
            while len(map) > k:
                if map.get(arr[i]) == 1:
                    del map[arr[i]]
                else:
                    map[arr[i]] -= 1
                i += 1

        j += 1

    return mx


# print(largestuniquestr(v, 3))

# Given a string s, find the length of the longest substring without repeating characters.


def largestuniquesubtring(arr):
    i = 0
    j = 0
    map = {}
    mx = 0

    while j < len(arr):

        if arr[j] in map:
            map[arr[j]] += 1

        elif arr[j] not in map:
            map[arr[j]] = 1

        if len(map) == sum(map.values()):
            mx = max(mx, len(map))

        elif len(map) < sum(map.values()):
            while len(map) < sum(map.values()):

                if map.get(arr[i]) == 1:
                    del map[arr[i]]

                else:
                    map[arr[i]] -= 1

                i += 1

        j += 1

    return mx


# print(largestuniquesubtring("abcabcbb"))


# John is at a toy store help him pick maximum number of toys.
# He can only select in a continuous manner and he can select only two types of toys.


def picktoys(arr):
    i = 0
    j = 0
    map = {}
    mx = 0

    arr = list(arr)

    while j < len(arr):

        if arr[j] in map:
            map[arr[j]] += 1

        elif arr[j] not in map:
            map[arr[j]] = 1

        if len(map) == 2:
            mx = max(mx, sum(map.values()))

        elif len(map) > 2:
            while len(map) > 2:
                if map.get(arr[i]) == 1:
                    del map[arr[i]]

                else:
                    map[arr[i]] -= 1

                i += 1
        j += 1

    return mx


# print(picktoys("abaccab"))

# Given two strings s and t, return the minimum window in s which will contain all
# the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

def maxwindowstr(arr, checkarr):
    i = 0
    j = 0
    j_index = 0
    i_index = 0
    map = {}
    mx = float('inf')

    arr = list(arr)
    checkarr = list(checkarr)

    for k in checkarr:
        if k not in map:
            map[k] = 1
        else:
            map[k] += 1

    count = len(map)

    while j < len(arr):

        if arr[j] in map:
            map[arr[j]] -= 1
            if map[arr[j]] == 0:
                count -= 1

        if count == 0:
            while count == 0:
                if j - i + 1 < mx:
                    j_index = j
                    i_index = i
                    mx = j - i + 1

                if arr[i] in map:
                    if map.get(arr[i]) == 0:
                        map[arr[i]] += 1
                        count += 1
                    elif map.get(arr[i]) < 0:
                        map[arr[i]] += 1
                i += 1

        j += 1

    return "".join(arr[i_index:j_index + 1])


# print(maxwindowstr('timetopractice', 'toc'))

# print(maxwindowstr("ADOBECODEBANC", "AEOBC"))

def isvalid(arr):
    ones = 0
    zeroes = 0
    for i in arr:
        if i == '1':
            ones += 1
        else:
            zeroes += 1

    return zeroes == ones


def checkones(arr):
    arr = list(arr)
    i_index = 0
    j_index = 0

    mx = 0

    for i in range(1, len(arr) + 1):
        for j in range(len(arr)):
            if isvalid(arr[j:j + i]):
                mx = max(mx, len(arr[j:j + i]))
                i_index = j
                j_index = j + i

    return "".join(arr[i_index:j_index + 1])


# s = '00011011110001100111'
s = "1110011"


# print(checkones(s))

def zeroones(arr):
    arr = list(arr)
    new_arr = []
    i_index = 0
    j_index = 0
    for i in arr:
        if i == '0':
            new_arr.append(-1)
        else:
            new_arr.append(1)

    map = {}
    mx = 0
    sum = 0
    map[sum] = -1

    for i in range(len(arr)):
        sum += new_arr[i]
        if sum in map:
            # mx = max(mx, i-map[sum])
            if i - map[sum] > mx:
                mx = i - map[sum]
                i_index = map[sum] + 1
                j_index = i + 1

        else:
            map[sum] = i

    # print(map)

    return "".join(arr[i_index:j_index])


print(zeroones(s))
