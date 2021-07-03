# Sorting and array using Recursion by using Induction-Hypothesis and Base condition Approach.

def sort(arr: list):
    if len(arr) == 1:
        return

    temp = arr.pop()

    sort(arr)

    insert(arr, temp)


def insert(arr, temp):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return

    ele = arr.pop()

    insert(arr, temp)

    arr.append(ele)


a = [1, 0, 5, 2]


# sort(a)
# print(a)

# Delete Middle Element of a Stack Using Recursion.
def mid_del(arr: list):
    mid = len(arr) // 2 + 1

    def rec_mid(arr: list, mid):
        if len(arr) == mid:
            arr.pop()
            return

        temp = arr.pop()

        rec_mid(arr, mid)

        arr.append(temp)

    rec_mid(arr, mid)


a = [1, 0, 5, 2, 6]


# mid_del(a)
# print(a)


def revStack(arr: list):
    if len(arr) == 1:
        return

    temp = arr.pop()

    revStack(arr)

    insert_rev(arr, temp)
    return


def insert_rev(arr: list, ele):
    if len(arr) == 0:
        arr.append(ele)
        return

    temp = arr.pop()

    insert_rev(arr, ele)

    arr.append(temp)
    return


# revStack(a)
# print(a)

# On the first row, we write a 0. Now in every subsequent row,
# we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

def kGrammar(n, k):
    if n == 1 and k == 1:
        return 0

    mid = (2 ** (n - 1)) // 2

    if k <= mid:
        return kGrammar(n - 1, k)

    else:
        return int(not (kGrammar(n - 1, k - mid)))


# print(kGrammar(4, 5))

# Program for Tower of Hanoi
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return

    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


# Driver code
n = 4

# TowerOfHanoi(n, 'A', 'C', 'B')


# Print all subsets of a String.

# Given the total number of persons n and a number k which indicates that k-1 persons are
# skipped and kth person is killed in circle. The task is to choose the place in the initial circle
# so that you are the last one remaining and so survive.

def josephus(n, k):
    circle = list(range(1, n + 1))

    def josephusUtil(circle, k, start=0):
        if len(circle) == 1:
            return circle[0]

        kill = (start + k - 1) % len(circle)
        circle.pop(kill)
        start = kill % len(circle)

        return josephusUtil(circle, k, start)

    return josephusUtil(circle, k)


print(josephus(40, 7))


# print all permutations of a string
ans = []


def permut(string, fixed=0):
    if fixed == len(string):
        ans.append(string)
        return

    for i in range(fixed, len(string)):
        string = string[:fixed] + string[i] + string[fixed:i] + string[i + 1:]
        permut(string, fixed + 1)


# permut("ABCDEF")
# print(ans)


# Given an array of non-negative integers nums, you are initially
# positioned at the first index of the array. Each element in the array represents
# your maximum jump length at that position. Determine if you are able
# to reach the last index.

def possible(arr, i, memo={}):
    if i >= len(arr):
        return False

    if i in memo:
        return memo[i]

    elif i == len(arr) - 1:
        return True

    for k in range(1, arr[i] + 1):
        if possible(arr, i + k, memo):
            memo[i] = True
            return memo[i]

    memo[i] = False
    return memo[i]


# print(possible([2, 3, 1, 1, 4], 0))

def countjump(arr, i=0, counter=0):
    if i >= len(arr) - 1:
        return 0

    for k in range(1, arr[i] + 1):
        counter = max(counter, countjump(arr, i + k))

    return 1 + counter


# print(countcanjump([2, 3, 1, 1, 4], 0, 0))

# You are given an array prices where prices[i] is the price of a
# given stock on the ith day. You want to maximize your profit by choosing a single
# day to buy one stock and choosing a different day in the future to sell that stock.

def beststock(arr):
    max_profit = 0

    for i in range(len(arr) - 1):
        mx = max(arr[i + 1:]) - arr[i]
        max_profit = max(max_profit, mx)

    return max_profit

# print(beststock([7, 1, 5, 3, 6, 4]))

# Print in combinations


def printCombination(arr, n, r):
    data = [0] * r
    combinationUtil(arr, data, 0, n - 1, 0, r)


def combinationUtil(arr, data, start, end, index, r):
    global ans
    if index == r:
        print(data)
        return

    i = start
    while i <= end and end - i + 1 >= r - index:
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1, end, index + 1, r)
        i += 1


printCombination([6, 4, 9, 7, 8], 5, 3)