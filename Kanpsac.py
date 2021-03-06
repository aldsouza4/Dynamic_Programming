

# 0 1 Knapsak

def knapsak(value_array, weight_array, weight, n):
    if t[n][weight] != -1:
        return t[n][weight]

    if weight == 0 or n == 0:
        return 0

    elif weight_array[n-1] > weight:
        t[n][weight] = knapsak(value_array, weight_array, weight, n-1)
        return t[n][weight]

    else:
        t[n][weight] = max(value_array[n-1] + knapsak(value_array, weight_array, weight - weight_array[n-1], n-1),
                   knapsak(value_array, weight_array, weight, n-1))
        return t[n][weight]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

t= [[-1 for i in range(W+1)] for j in range(n+1)]
print(knapsak(val, wt, W, n))

# 0 1 knapsack top Down

def knapsack(value_array, weight_array, weight):

    n= len(weight_array)

    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    for i in range(n+1):
        for j in range(weight+1):

            if i == 0 or j == 0:
                t[i][j] = 0

            elif weight_array[i-1] <= j:
                t[i][j] = max(value_array[i - 1] + t[i - 1][j - weight_array[i - 1]],
                              t[i - 1][j])

            else:
                t[i][j] = t[i-1][j]

    print(t[n][weight])


knapsack(val, wt, W)



