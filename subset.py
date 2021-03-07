# subset question
# without repetition
def subset(arr, target, n):
    if target == 0:
        return True

    elif n == 0:
        return False

    elif arr[n - 1] > target:
        return subset(arr, target, n - 1)

    else:
        return subset(arr, target - arr[n - 1], n - 1) or subset(arr, target, n - 1)


set = [1, 2, 3, 3]
su = 6
n = len(set)


# Equal Sum Partition Problem
# Partition problem is to determine whether a given set can be
# partitioned into two subsets such that the sum of elements in both subsets is same.

def equal_subset(arr, target, n):
    if target == 0:
        return True

    elif n == 0:
        return False

    elif arr[n - 1] > target:
        return equal_subset(arr, target, n - 1)

    else:
        return equal_subset(arr, target - arr[n - 1], n - 1) or equal_subset(arr, target, n - 1)


sum_ = sum(set) // 2


# if sum is not an int ... return false

# print(equal_subset(set, sum_, n ))


# Count of subsets sum with a Given sum
# Given an array arr[] of length N and an
# integer X, the task is to find the number of subsets with sum equal to X.

def countTarget(arr, target):
    n = len(arr)
    t = [[0 for i in range(target + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(target + 1):

            if j == 0:
                t[i][j] = 1
            elif i == 0:
                t[i][j] = 0

            elif arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i - 1]]

            else:
                t[i][j] = t[i - 1][j]

    return t[n][target]


# print(countTarget(arr=set, target=6))

# Sum of subset differences
# Given a set of integers, the task is to divide it into two sets S1 and S2
# such that the absolute difference between their sums is minimum.
# If there is a set S with n elements, then if we assume Subset1 has m elements,
# Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

def small_sum(arr, target):
    n = len(arr)
    t = [[0 for i in range(target + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(target + 1):

            if j == 0:
                t[i][j] = True
            elif i == 0:
                t[i][j] = False

            elif arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] or t[i - 1][j - arr[i - 1]]

            else:
                t[i][j] = t[i - 1][j]

    v = t[-1]
    check = []
    for i in range(len(v) // 2):
        if v[i]:
            check.append(i)
    mn = float('inf')
    for i in check:
        mn = min(mn, target - 2 * i)

    return mn


array = [1, 1, 2, 3]
sum_range = sum(array)

# print(small_sum(array, sum_range))
real_diff = 1

# Count the number of subset with a given difference
def count_subset_diff(arr, target, n):
    t = [[0 for i in range(target + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(target + 1):

            if j == 0:
                t[i][j] = 1

            elif i == 0:
                t[i][j] = 0

            elif arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i - 1]]

            else:
                t[i][j] = t[i - 1][j]

    v = t[-1]

    for i in range(len(v) // 2):
        if target - 2 * i == real_diff:
            print(v[i])


# count_subset_diff(array, sum_range, 4)

