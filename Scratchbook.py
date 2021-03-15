# def countcanjump(arr, i=0):
#     if i >= len(arr):
#         return False
#
#     elif i == len(arr) - 1:
#         return True
#
#     for k in range(1, arr[i] + 1):
#         if countcanjump(arr, i + k):
#             return True
#
#     return False
#
#
# print(countcanjump([2, 3, 1, 1, 4]))




# print(countjump([2, 3, 1, 1, 4]))


def climbsteps(n, memo=None):

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 1

    elif n < 0:
        return 0

    memo[n] = climbsteps(n-1) + climbsteps(n-2)
    return memo[n]

print(climbsteps(3))
