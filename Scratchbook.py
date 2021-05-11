def smallest_sum(arr):
    add = sum(arr)

    dp = [[-1 for i in range(add+1)] for i in range(len(arr)+1)]

    for i in range(len(arr)+1):
        for j in range(add+1):

            if j == 0:
                dp[i][j] = True

            elif i == 0:
                dp[i][j] = False

            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

            elif arr[i-1] > j:
                dp[i][j] = dp[i-1][j]

    vector = dp[-1]
    check = []
    for i in range(len(vector)//2+1):
        if vector[i]:
            check.append(i)

    mn = float('inf')

    for i in check:
        mn = min(mn, add - i*2)

    print(mn)


smallest_sum([1, 2, 1, 3, 3])

