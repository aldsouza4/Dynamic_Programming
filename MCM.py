# Matrix Chain Multiplication using Recursion
#  Given a sequence of matrices, find the most efficient way to multiply these matrices together.
# The problem is not actually to  perform the multiplications, but merely to decide in which
# order to perform the multiplications.


def mcm(arr, i, j):
    """

    :param arr:given array
    :param i: 2nd index
    :param j: last index or len(arr-1)
    :return:
    """
    if i >= j:
        return 0

    mn = float('inf')

    for k in range(i, j):
        temp = mcm(arr, i, k) + mcm(arr, k + 1, j) + (arr[i - 1] * arr[k] * arr[j])

        mn = min(mn, temp)

    return mn


array = [40, 20, 30, 10, 30]
# print(mcm(array, 1, len(array)-1))


# Meomized MCM
t = [[-1 for i in range(1000)] for i in range(1000)]


def mem_MCM(arr, i, j):
    if t[i][j] != -1:
        return t[i][j]

    elif i >= j:
        return 0

    mn = float('inf')

    for k in range(i, j):

        if t[i][k] != -1:
            t1 = t[i][k]

        else:
            t1 = mem_MCM(arr, i, k)

        if t[k + 1][j] != -1:
            t2 = t[k + 1][j]

        else:
            t2 = mem_MCM(arr, k + 1, j)

        temp = t1 + t2 + (arr[i - 1] * arr[k] * arr[j])

        mn = min(temp, mn)

    return mn


# print(mem_MCM(array, 1, len(array)-1))


# Palindrome Partitioning using Recursion
# Given a string, a partitioning of the string is a palindrome partitioning
# if every substring of the partition is a palindrome.

s = "ababbbabbababa"
n = len(s)


def isPalindrome(x):
    return x == x[::-1]


def palindromePartition(string, i, j):
    if t[i][j] != -1:
        return t[i][j]

    if i >= j:
        return 0

    if isPalindrome(string[i:j + 1]):
        return 0

    mn = float('inf')

    for k in range(i, j):
        if t[i][k] != -1:
            t1 = t[i][k]

        else:
            t1 = palindromePartition(string, i, k)

        if t[k + 1][j] != -1:
            t2 = t[k + 1][j]

        else:
            t2 = palindromePartition(string, k + 1, j)

        temp = t1 + t2 + 1

        mn = min(temp, mn)

    return mn


# print(palindromePartition(s, 0, n-1))


# Scramble String using Recursion
# Given a string s1, we may represent it as a binary tree by
# partitioning it to two non-empty substrings recursively.

def scramble(str1, str2):
    if str1 == str2:
        return True

    if len(str1) != len(str2):
        return False

    if sorted(str1) != sorted(str2):
        return False

    n = len(str1)

    if not n:
        return True

    flag = False

    for i in range(1, n):

        cond1 = (scramble(str1[-i:], str2[:-i]) == True) and (scramble(str1[:-i], str2[-i:]) == True)
        cond2 = (scramble(str1[:i], str2[:i]) == True) and (scramble(str1[i:], str2[i:]) == True)

        if cond1 or cond2:
            flag = True
            break

    return flag


# print(scramble("great", "rgeat"))

# Egg Dropping using Recursion
# Problem statement: You are given N floor and K eggs. You have to minimize the number of times
# you have to drop the eggs to find the critical floor where critical floor means the floor
# beyond which eggs start to break. Assumptions of the problem:


def eggBreak(egg, floor):
    if floor == 0 or floor == 1:
        return floor

    if egg == 1:
        return floor

    mn = float('inf')

    for k in range(1, floor + 1):
        temp = 1 + max(eggBreak(egg - 1, k - 1),
                       eggBreak(egg, floor - k))

        mn = min(temp, mn)

    return mn


eggs = 2
floor = 4

# t = [[-1 for i in range(floor + 1)] for i in range(eggs + 1)]
print(eggBreak(2, 20))
