ar = [50, 3, 10, 7, 40, 80]


def longestincsubseq(arr):
    if arr is None:
        return

    n = len(arr)

    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        dp[i] = 1

        for j in range(i-1, -1, -1):
            if arr[j] > arr[i]:
                continue
            possible_ans = dp[j] + 1
            if possible_ans > dp[i]:
                dp[i] = possible_ans

    return dp

print(longestincsubseq(ar))