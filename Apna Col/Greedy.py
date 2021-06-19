from heapq import *
import heapq


# min number of coins
def notes(notes_arr, amount):
    notes_arr = sorted(notes_arr, reverse=True)

    i = 0
    ans = 0
    while i < len(notes_arr):
        if amount >= notes_arr[i]:
            amount -= notes_arr[i]
            ans += 1
        else:
            i += 1

    return ans


# print(notes([1, 2, 5, 10, 20, 50, 100, 200, 500, 2000], 350))

# Frac kapsack

class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


# Greedy Approach
def getMaxValue(wt, val, capacity):
    """function to get maximum value """
    iVal = []
    for i in range(len(wt)):
        iVal.append(ItemValue(wt[i], val[i], i))

    # sorting items by value
    iVal.sort(reverse=True)

    totalValue = 0
    for i in iVal:
        curWt = int(i.wt)
        curVal = int(i.val)
        if capacity - curWt >= 0:
            capacity -= curWt
            totalValue += curVal
        else:
            fraction = capacity / curWt
            totalValue += curVal * fraction
            capacity = int(capacity - (curWt * fraction))
            break
    return totalValue


# wt = [10, 40, 20, 30]
# val = [60, 40, 100, 120]
# capacity = 50
# print(getMaxValue(wt, val, capacity))

def optimalmerge(arr):
    if arr is None:
        return
    heap = []

    for i in arr:
        heappush(heap, i)

    cost = 0
    while True:
        x = heappop(heap)

        if len(heap) == 0:
            return cost

        y = heappop(heap)
        ans = x + y
        cost += ans
        heappush(heap, ans)


print(optimalmerge([2, 4, 5, 7]))


# https://www.spoj.com/problems/EXPEDI/
# fuel_stops = [[distance from the destination, fuel available at the stop]]

def cowstruck(fuel_stops: list, total_distance: int, initial_fuel: int):
    # making the first element of the list to distance from the truck
    for i in range(len(fuel_stops)):
        fuel_stops[i][0] = total_distance - fuel_stops[i][0]

    fuel_stops.sort(key=lambda x: x[0])

    flag = False
    stops = 0
    curr_fuel = initial_fuel

    heap = []

    for i in fuel_stops:
        if curr_fuel >= total_distance:
            return stops

        while curr_fuel < i[0]:
            if len(heap) == 0:
                flag = True
                break

            stops += 1
            curr_fuel += heapq.heappop(heap)

            if flag:
                break

        if flag:
            print(flag)
            continue

        heapq.heappush(heap, i[1])

        while len(heap) != 0 and curr_fuel < total_distance:
            curr_fuel += heapq.heappop(heap)
            stops += 1

        if curr_fuel < total_distance:
            print(False)
            continue

    return stops

# print(cowstruck([[4, 4], [5, 2], [11, 5], [15, 10]], 25, 10))

# max and min diff in array


def maxmin(array: list):
    if array is None:
        return

    n = len(array)

    array.sort()

    mn = 0
    mx = 0

    for i in range(n//2):
        mx += (array[i + n//2] - array[i])
        mn += (array[2 * i + 1] - array[2*i])

    return mn, mx


# print(maxmin([12, -3, 10, 0]))
