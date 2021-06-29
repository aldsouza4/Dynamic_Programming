# print length of largest increasing subsequence
def lis(arr):
    n = len(arr)
    if n == 0:
        return

    dp = [-1 for i in range(n)]

    def lis_util(arr, n):
        if dp[n] != -1:
            return dp[n]

        dp[n] = 1

        for i in range(n):
            if arr[n] > arr[i]:
                dp[n] = max(dp[n], 1 + lis_util(arr, i))

        return dp[n]

    return lis_util(arr, n-1)


# print(lis([1, 4, 2, 5, 3]))
