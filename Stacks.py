# Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array.
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

    for i in range(len(array)-1, -1, -1):

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


