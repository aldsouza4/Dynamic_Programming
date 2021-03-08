# Longest Common Subsequence Problem solution using recursion
# Given two sequences, find the length of longest
# subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order,
# but not necessarily contiguous.

def lcs(str1, str2, m, n):
    if m==0 or n==0:
        return 0

    if str1[m-1] == str2[n-1]:
        return 1 + lcs(str1, str2, m-1, n-1)

    else:
        return max(lcs(str1, str2, m-1, n),
                   lcs(str1, str2, m, n-1))


a = "AGGTAB"
b = "GXTXAYB"
m = len(a)
n = len(b)

# print(lcs(a, b, m, n))


def lcs_memoized(str1, str2, m, n):
    if t[m][n] != -1:
        return t[m][n]

    elif m==0 or n==0:
        return 0

    elif str1[m-1] == str2[n-1]:
        t[m][n] = 1+lcs(str1, str2, m-1, n-1)
        return t[m][n]

    else:
        t[m][n] =max(lcs(str1, str2, m-1, n),
                   lcs(str1, str2, m, n-1))
        return t[m][n]


t = [[-1 for i in range(n+1)] for j in range(m+1)]

# print(lcs_memoized(a, b, m, n))


#LCS Top Down approach

def lcs_TopDown(str1, str2, m, n):
    t = [[-1 for i in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i == 0 or j == 0:
                t[i][j] = 0

            elif str1[i-1] == str2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]

            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])


    return t[m][n]

# print(lcs_TopDown(a, b, m, n))

# Longest Common Substring(Dynamic Programming)
# Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.

def substring(str1, str2, m, n):
    t = [[-1 for i in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                t[i][j] = 0

            elif str1[i - 1] == str2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]

            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    mx = 0
    for i in t:
        for k in i:
            mx = max(mx, k)

    return mx


X = "GeeksforGeeks"
y = "GeeksQuiz"
m = len(X)
n = len(y)

# print(substring(X, y, m, n))


# Printing Longest Common Subsequence
# Given two sequences, print the longest subsequence present in both of them.


def lcs_TopDown_print(str1, str2, m, n):
    t = [[-1 for i in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i == 0 or j == 0:
                t[i][j] = 0

            elif str1[i-1] == str2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]

            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])


    i = m
    j = n
    new = ""
    while i>0 and j>0:
        if str1[i-1] == str2[j-1]:
            new += str1[i-1]
            i -= 1
            j -= 1

        else:
            if t[i-1][j] > t[i][j-1]:
                i -= 1

            else:
                j -= 1

    return new[::-1]


A = "ABCDGH"
B = "AEDFHR"
m = len(A)
n = len(B)

# print(lcs_TopDown_print(A,B, m, n))

# Shortest Common Supersequence
# Given two strings str1 and
# str2, find the shortest string that has both str1 and str2 as subsequences.

def supersequence(str1, str2, m, n):

    leghtLCS = lcs(str1, str2, m, n)

    return m + n - leghtLCS

# print(supersequence(A, B, m, n))

# Minimum number of deletions and insertions to transform one string into another
# Given two strings ‘str1’ and ‘str2’ of size m and n respectively.
# The task is to remove/delete and insert minimum number of characters from/in str1
# so as to transform it into str2. It could be possible that the same character needs
# to be removed/deleted from one point of str1 and inserted to some another point.

def minDelInsetion(str1, str2, m, n):
    leghtLCS = lcs(str1, str2, m, n)

    dels = m - leghtLCS
    ins = n - leghtLCS

    return dels + ins

str1 = "geeksforgeeks"
str2 = "geeks"

# print(minDelInsetion(str1, str2, len(str1), len(str2)))


