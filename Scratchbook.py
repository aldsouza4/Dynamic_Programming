def ngr(arr):
    stack = []
    result_arr = []

    i = len(arr) - 1

    while i != -1:

        if len(stack) == 0:
            result_arr.append(-1)

        elif stack[-1] > arr[i]:
            result_arr.append(stack[-1])

        elif stack[-1] < arr[i]:
            while len(stack) > 0 and stack[-1] < arr[i]:
                stack.pop()

            if len(stack) == 0:
                result_arr.append(-1)

            else:
                result_arr.append(stack[-1])

        stack.append(arr[i])
        i -= 1

    return result_arr[::-1]


def nsl(arr):
    stack = []
    result_arr = []

    for i in range(len(arr)):

        if len(stack) == 0:
            result_arr.append(-1)

        elif stack[-1] < arr[i]:
            result_arr.append(stack[-1])

        elif stack[-1] > arr[i]:

            while stack[-1] > arr[i]:
                stack.pop()

            if len(stack) == 0:
                result_arr.append(-1)

            else:
                result_arr.append(stack[-1])

        stack.append(arr[i])

    return result_arr


# print(nsl([1, 3, 2, 4]))



def stockspan(arr):

    result_arr = []
    stack = []

    for i in range(len(arr)):

        if len(stack) == 0:
            result_arr.append(1)

        elif arr[stack[-1]] > arr[i]:
            result_arr.append(1)

        elif arr[stack[-1]] < arr[i]:

            while arr[stack[-1]] < arr[i]:
                stack.pop()

            if len(stack) == 0:
                result_arr.append(1)

            else:
                result_arr.append(i - stack[-1])

        stack.append(i)

    return result_arr


p = [100, 80, 60, 70, 60, 75, 85]
# print(stockspan(p))















