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

    men = list(range(1, n+1))

    def killmen(arr:list, k, start):
        if len(arr) == 1:
            return arr[0]

        siz = len(arr)
        i = (start+k-1)%siz
        arr.remove(arr[i])
        return killmen(arr, k, i+1)

    return killmen(men, k-1, 1)


# print(josephus(40, 7))


