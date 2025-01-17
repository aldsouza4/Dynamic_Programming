# 0 1 Knapsak

def knapsak(value_array, weight_array, weight, n):
    if t[n][weight] != -1:
        return t[n][weight]

    if weight == 0 or n == 0:
        return 0

    elif weight_array[n - 1] > weight:
        t[n][weight] = knapsak(value_array, weight_array, weight, n - 1)
        return t[n][weight]

    else:
        t[n][weight] = max(value_array[n - 1] + knapsak(value_array, weight_array, weight - weight_array[n - 1], n - 1),
                           knapsak(value_array, weight_array, weight, n - 1))
        return t[n][weight]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

t = [[-1 for i in range(W + 1)] for j in range(n + 1)]


# print(knapsak(val, wt, W, n))

# 0 1 knapsack top Down

def knapsack(value_array, weight_array, weight):
    n = len(weight_array)

    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(weight + 1):

            if i == 0 or j == 0:
                t[i][j] = 0

            elif weight_array[i - 1] <= j:
                t[i][j] = max(value_array[i - 1] + t[i - 1][j - weight_array[i - 1]],
                              t[i - 1][j])

            else:
                t[i][j] = t[i - 1][j]

    print(t[n][weight])


# knapsack(val, wt, W)


# Unbounded knapsac

def unbounded(arr, target, n):
    if target == 0:
        return True

    elif n == 0:
        return False

    elif arr[n - 1] <= target:
        return unbounded(arr, target - arr[n - 1], n) or unbounded(arr, target, n - 1)

    else:
        return unbounded(arr, target, n - 1)


array = [4, 5]
tar = 170


# print(unbounded(array, tar, 2))

# Rod Cutting Problem
#  Given a rod of length n inches and an array of prices that contains prices of all
#  pieces of size smaller than n.
#  Determine the  maximum value obtainable by cutting up the rod and selling the pieces


def rod_cutting(val, cuts, length, n):
    if length == 0 or n == 0:
        return 0

    elif cuts[n - 1] <= length:
        return max(rod_cutting(val, cuts, length, n - 1),
                   val[n - 1] + rod_cutting(val, cuts, length - cuts[n - 1], n))

    else:
        return rod_cutting(val, cuts, length, n - 1)


cut = list(range(1, 8 + 1))
val = [1, 5, 8, 9, 10, 17, 17, 20]
l = 8
x = len(val)


# print(rod_cutting(val, cut, l, x))

# Coin Change Problem Maximum Number of ways
# Given a value N, if we want to make change for N cents, and we have infinite supply of each
# of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.


def coinchange_max(arr, target, n):
    if target == 0:
        return 1

    elif n == 0:
        return 0

    elif arr[n - 1] <= target:
        return coinchange_max(arr, target - arr[n - 1], n) + coinchange_max(arr, target, n - 1)

    else:
        return coinchange_max(arr, target, n - 1)


N = 4
coi = [1, 2, 3]


# print(coinchange_max(coi, N, 3))

# Coin Change Problem Minimum Numbers of coins
# Given a value V, if we want to make change for V cents, and we have infinite
# supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to


def min_coinchange(arr, target):
    n = len(arr)

    t = [[-1 for i in range(target + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(target + 1):

            if i == 0:
                t[i][j] = float('inf') - 1

            elif j == 0:
                t[i][j] = 0

            elif i == 1 and j > 0:
                if j % arr[i - 1] == 0:
                    t[i][j] = arr[i - 1] // j
                else:
                    t[i][j] = float('inf') - 1

            elif arr[i - 1] <= j:
                t[i][j] = min(1 + t[i - 1][j - arr[i - 1]], t[i - 1][j])

            else:
                t[i][j] = t[i - 1][j]

    return t[n][target]


lo = [25, 10, 5]
V = 30
print(min_coinchange(lo, V))

# fractional knapsac

wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50


def fracknapsack(val_arry, wt_arry, weight):
    ratio = []
    for i in range(len(val_arry)):
        ratio.append(val_arry[i] / wt_arry[i])

    # print(ratio.index(max(ratio)))
    mx_weight = 0

    while weight > 0:
        ind = ratio.index(max(ratio))

        if weight >= wt_arry[ind]:

            weight -= wt_arry[ind]
            mx_weight += val_arry[ind]

            wt_arry.remove(wt_arry[ind])
            val_arry.remove(val_arry[ind])
            ratio.remove(ratio[ind])

        else:
            temp = (weight / wt_arry[ind]) * val_arry[ind]
            mx_weight += temp
            weight -= wt_arry[ind]

    return mx_weight


def fractionalknapsack(W, Items, n):
    shop = []

    # for i in range(n):
    #     shop.append([Items[i].value, Items[i].weight, Items[i].value/Items[i].weight])

    for i in range(n):
        shop.append([Items[0][i], Items[1][i], Items[0][i] / Items[1][i]])

    shop.sort(key=lambda a: a[2], reverse=True)

    sack = 0
    i = 0

    while i < n:
        if shop[i][1] <= W:
            sack += shop[i][0]
            W -= shop[i][1]
        else:
            break
        i += 1

    sack += (W * shop[i][0] / shop[i][1])


# print(fracknapsack(val, wt, capacity))

def twoSum(arr, target, n=4):
    if n == 0 and target != 0:
        return False

    elif n == 0 and target == 0:
        return True

    for i in arr:
        if twoSum(arr, target - i, n - 1):
            return True

    return False

# print(twoSum([3, 5, 6, 8, 2, 3], 10))
