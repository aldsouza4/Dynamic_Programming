# Given an array, print the Next Greater Element (NGE) for every element.
# The Next greater Element for an element x is the first greater element on the right side of x in array.
# Elements for which no greater element exist, consider next greater element as -1.


def NGR(array):
    stack = []
    result_array = []

    for i in range(len(array) - 1, -1, -1):
        if len(stack) == 0:
            result_array.append(-1)

        elif len(stack) > 0 and stack[-1] > array[i]:
            result_array.append(stack[-1])

        elif len(stack) > 0 and stack[-1] <= array[i]:

            while len(stack) > 0 and stack[-1] <= array[i]:
                stack.pop()

            if len(stack) == 0:
                stack.append(-1)

            else:
                result_array.append(stack[-1])

        stack.append(array[i])

    return result_array[::-1]


# print(NGR([1, 3, 2, 4]))


# Given an array of integers, find the closest (not considering distance, but value)
# greater on left of every element. If an element has no greater on the left side,print -1.


def NGL(array):
    stack = []
    result_array = []

    for i in range(len(array)):
        if len(stack) == 0:
            result_array.append(-1)

        elif len(stack) > 0 and stack[-1] > array[i]:
            result_array.append(stack[-1])

        elif len(stack) > 0 and stack[-1] <= array[i]:

            while len(stack) > 0 and stack[-1] <= array[i]:
                stack.pop()

            if len(stack) == 0:
                result_array.append(-1)

            else:
                result_array.append(stack[-1])

        stack.append(array[i])

    return result_array


# print(NGL([1, 3, 2, 4]))


def NSL(array):
    stack = []
    result_array = []

    for i in range(len(array)):

        if len(stack) == 0:
            result_array.append(-1)

        elif len(stack) > 0 and stack[-1] < array[i]:
            result_array.append(stack[-1])

        elif len(stack) > 0 and stack[-1] >= array[i]:

            while len(stack) > 0 and stack[-1] >= array[i]:
                stack.pop()

            if len(stack) == 0:
                result_array.append(-1)

            else:
                result_array.append(stack[-1])

        stack.append(array[i])

    return result_array


# print(NSL([1, 3, 2, 4]))


def NSR(array):
    stack = []
    result_array = []

    for i in range(len(array) - 1, -1, -1):

        if len(stack) == 0:
            result_array.append(-1)

        elif len(stack) > 0 and stack[-1] < array[i]:
            result_array.append(stack[-1])

        elif len(stack) > 0 and stack[-1] >= array[i]:

            while len(stack) > 0 and stack[-1] >= array[i]:
                stack.pop()

            if len(stack) == 0:
                result_array.append(-1)

            else:
                result_array.append(stack[-1])

        stack.append(array[i])

    return result_array[::-1]


# print(NSR([1, 3, 2, 4]))

# The stock span problem is a financial problem where we have a series of n daily price
# quotes for a stock and we need to calculate span of stock’s price for all n days.

def stockspan(arr):
    stack = []
    result_array = []

    for i in range(len(arr)):

        if len(stack) == 0:
            result_array.append(1)

        elif arr[stack[-1]] > arr[i]:
            result_array.append(1)

        elif arr[stack[-1]] <= arr[i]:

            while arr[stack[-1]] <= arr[i]:
                stack.pop()

            if len(stack) == 0:
                result_array.append(i)

            else:
                result_array.append(i - stack[-1])

        stack.append(i)

    return result_array


p = [100, 80, 60, 70, 60, 75, 85]


# print(stockspan(p))

# Find the largest rectangular area possible in a given histogram where the largest
# rectangle can be made of a number of contiguous bars. For simplicity, assume that
# all bars have same width and the width is 1 unit.

def histogramArea(arr):
    def index_nsl(arr):

        stack = []
        result_array = []

        for i in range(len(arr)):

            if len(stack) == 0:
                result_array.append(-1)

            elif len(stack) > 0 and arr[stack[-1]] < arr[i]:
                result_array.append(stack[-1])

            elif len(stack) > 0 and arr[stack[-1]] >= arr[i]:

                while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                    stack.pop()

                if len(stack) == 0:
                    result_array.append(-1)

                else:
                    result_array.append(stack[-1])

            stack.append(i)

        return result_array

    def index_nsr(arr):

        stack = []
        result_array = []

        for i in range(len(arr) - 1, -1, -1):

            if len(stack) == 0:
                result_array.append(len(arr))

            elif len(stack) > 0 and arr[stack[-1]] < arr[i]:
                result_array.append(i + 1)

            elif len(stack) > 0 and arr[stack[-1]] >= arr[i]:

                while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                    stack.pop()

                if len(stack) == 0:
                    result_array.append(len(arr))

                else:
                    result_array.append(stack[-1])

            stack.append(i)

        return result_array[::-1]

    sm_right = index_nsr(arr)
    sm_left = index_nsl(arr)

    mx = 0
    for i, j, k in zip(sm_right, sm_left, range(len(arr))):
        temp = arr[k] * (i - j - 1)
        mx = max(mx, temp)

    return mx


r = [6, 2, 5, 4, 5, 1, 6]


# print(histogramArea(r))

# Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s.

def area_matrix(mat):
    mx = 0
    temp_mat = [0 for i in range(len(mat[0]))]

    for i in range(len(mat)):

        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                temp_mat[j] = 0
            else:
                temp_mat[j] = temp_mat[j] + mat[i][j]

        mx = max(mx, histogramArea(temp_mat))

    return mx


matrix = [[0, 1, 1, 0],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 0, 0]]


# print(area_matrix(matrix))


# Given n non-negative integers representing an elevation map where the width of each
# bar is 1, compute how much water it is able to trap after raining.

def rainTrap(arr):
    water = 0
    for i in range(1, len(arr) - 1):
        l = max(arr[:i])
        r = max(arr[i + 1:])

        water += min(l, r) - arr[i]

    return water


w = [3, 0, 0, 2, 0, 4]

print(rainTrap(w))


# Design a Data Structure SpecialStack that supports all the stack operations like
# push(), pop(), isEmpty(), isFull() and an additional operation getMin() which
# should return minimum element from the SpecialStack.
# All these operations of SpecialStack must be O(1).

class Stack():

    def __init__(self):
        self.stack = []
        self.min_ele = 0

    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.min_ele = x

        else:
            if x >= self.min_ele:
                self.stack.append(x)

            elif x < self.min_ele:
                self.stack.append(2 * x - self.min_ele)
                self.min_ele = x

    def pop(self):
        if len(self.stack) == 0:
            return -1

        else:
            if self.stack[-1] >= self.min_ele:
                return self.stack.pop()

            elif self.stack[-1] < self.min_ele:
                self.min_ele = 2 * self.min_ele - self.stack[-1]
                return self.stack.pop()


t = Stack()

t.push(8)
t.push(4)
t.push(5)
t.push(6)
t.push(3)

# print(t.min_ele)
# t.pop()
# print(t.min_ele)
