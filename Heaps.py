from heapq import *

l = [7, 10, 4, 3, 20, 15]


# Returnt the k smallest element in the array

def kminheap(arr, k):
    arr = [-1 * x for x in arr]
    hp = []

    for i in arr:
        heappush(hp, i)

        if len(hp) > k:
            heappop(hp)

    return hp[0] * -1


# print(kminheap(arr=l, k=3))


# Write an efficient program for printing k largest elements in an array.
# Elements in array can be in any order.

def klargestele(arr, k):
    minhp = []

    for i in arr:
        heappush(minhp, i)

        if len(minhp) > k:
            heappop(minhp)

    return minhp


# print(klargestele([1, 23, 12, 9, 30, 2, 50], 3))


# Given an array of n elements, where each element is at most k away
# from its target position, devise an algorithm that sorts in O(n log k) time

def sorktKarray(arr, k):
    final_array = []
    min_heap = []

    for i in arr:
        heappush(min_heap, i)

        if len(min_heap) > k:
            final_array.append(heappop(min_heap))

    while len(min_heap) != 0:
        final_array.append(heappop(min_heap))

    return final_array


# print(sorktKarray([6, 5, 3, 2, 8, 10, 9], 3))


# Given an unsorted array and two numbers x and k, find k closest values to x

ar = [10, 2, 14, 4, 7, 6]
x = 5
k = 3


def closeskarr(arr, x, k):
    heap = []

    for i in arr:
        heappush(heap, (-1 * abs(i - x), i))

        if len(heap) > k:
            heappop(heap)

    return [x[1] for x in heap]


# print(closeskarr(ar, x, k))


# Given an array of n numbers. Your task is to read numbers from the array and keep at-most K
# numbers at the top (According to their decreasing frequency) every time a new number is read.
# We basically need to print top k numbers sorted by frequency when input stream has included k
# distinct elements, else need to print all distinct elements sorted by frequency.

def kFrequentnumbers(arr, k):
    map = {}
    for i in arr:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    heap = []

    for i in map:
        heappush(heap, (map[i], i))
        if len(heap) > k:
            heappop(heap)

    for i in heap:
        print("{} accrued {} times".format(i[1], i[0]))


# print(kFrequentnumbers([5, 5, 2, 1, 3, 5, 2], 3))

# Print the elements of an array in the increasing frequency if 2
# numbers have same frequency then print the one which came first.

from collections import OrderedDict


def frequencySort(arr):
    map = {}

    for i in arr:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    final_array = []
    heap = []

    for i in map:
        heappush(heap, [-1 * map[i], i])

    for j in heap:
        while j[0] != 0:
            final_array.append(j[1])
            j[0] += 1

    return final_array


# print(frequencySort([2, 5, 2, 8, 5, 6, 8, 8]))


def closestOrigin(points, k):
    distance_arr = []
    for i in points:
        distance_arr.append([round((i[0] ** 2 + i[1] ** 2) ** 0.5, 3), i])

    heap = []
    for i in distance_arr:
        heappush(heap, [i[0] * -1, i[1]])
        if len(heap) > k:
            heappop(heap)

    return [x[1] for x in heap]


point = [[3, 3], [5, -1], [-2, 4]]


# print(closestOrigin(point, 2))

# There are given n ropes of different lengths, we need to connect these
# ropes into one rope. The cost to connect two ropes is equal to sum of their
# lengths. We need to connect the ropes with minimum cost.

def minRopes(arr):
    heap = []

    for i in arr:
        heappush(heap, i)

    while len(heap) != 1:
        x, y = heappop(heap), heappop(heap)
        tcost = x + y
        heappush(heap, tcost)

    return heap[0]


# print(minRopes([4, 3, 2, 6]))


# Given an array of integers and two numbers k1 and k2. Find the sum of all
# elements between given two k1’th and k2’th smallest elements of the array.
# It may  be assumed that all elements of array are distinct.

def sumbetweenK(arr, k1, k2):
    def kSmallestnumber(arr, k):
        heap = []
        for i in arr:
            heappush(heap, -i)

            if len(heap) > k:
                heappop(heap)

        return -heap[0]

    kone = kSmallestnumber(arr, k1)
    ktwo = kSmallestnumber(arr, k2)
    sum = 0

    for i in arr:
        if kone < i < ktwo or ktwo < i < kone:
            sum += i

    return sum


array = [20, 8, 22, 4, 12, 10, 14]
k1 = 3
k2 = 6

# print(sumbetweenK(array, k1, k2))
