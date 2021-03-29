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
