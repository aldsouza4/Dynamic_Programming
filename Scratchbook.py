def NGR(arr):
    resultArr = []
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        if len(stack) == 0:
            resultArr.append(-1)

        elif stack[-1] > arr[i]:
            resultArr.append(stack[-1])

        elif stack[-1] < arr[i]:
            while len(stack) > 0 and stack[-1] < arr[i]:
                stack.pop()

            if len(stack) == 0:
                resultArr.append(-1)

            else:
                resultArr.append(stack[-1])
        stack.append(arr[i])

    return resultArr[::-1]


# print(NGR([11, 13, 21, 3]))

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


def NSL(arr):
    stack = []
    resultArr = []

    for i in range(len(arr)):
        if len(stack) == 0:
            resultArr.append(-1)

        elif stack[-1] < arr[i]:
            resultArr.append(stack[-1])

        elif stack[-1] > arr[i]:
            while len(stack) > 0 and stack[-1] > arr[i]:
                stack.pop()

            if len(stack) == 0:
                resultArr.append(-1)

            else:
                resultArr.append(stack[-1])
        stack.append(arr[i])

    return resultArr


# print(NSL([4, 5, 2, 10, 8]))


def stockSpan(arr):
    stack = []
    resultArr = []

    for i in range(len(arr)):
        if len(stack) == 0:
            resultArr.append(1)

        elif arr[stack[-1]] > arr[i]:
            resultArr.append(i - stack[-1])

        elif arr[stack[-1]] < arr[i]:
            while len(stack) > 0 and arr[stack[-1]] < arr[i]:
                stack.pop()

            if len(stack) == 0:
                resultArr.append(1)

            else:
                resultArr.append(i - stack[-1])

        stack.append(i)

    return resultArr


# print(stockSpan([100, 80, 60, 70, 60, 75, 85]))


def HistogramArea(arr):
    def NSL_index(arr):
        stack = []
        resarr = []

        for i in range(len(arr)):
            if len(stack) == 0:
                resarr.append(-1)

            elif arr[stack[-1]] < arr[i]:
                resarr.append(stack[-1])

            elif arr[stack[-1]] > arr[i]:
                while len(stack) > 0 and arr[stack[-1]] > arr[i]:
                    stack.pop()

                if len(stack) == 0:
                    resarr.append(-1)

                else:
                    resarr.append(stack[-1])

            stack.append(i)

        return resarr

    def NSR_index(arr):
        stack = []
        resarr = []

        for i in range(len(arr) - 1, -1, -1):
            if len(stack) == 0:
                resarr.append(len(arr))

            elif arr[stack[-1]] < arr[i]:
                resarr.append(stack[-1])

            elif arr[stack[-1]] >= arr[i]:
                while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                    stack.pop()

                if len(stack) == 0:
                    resarr.append(len(arr))

                else:
                    resarr.append(stack[-1])

            stack.append(i)

        return resarr[::-1]

    left = NSL_index(arr)
    right = NSR_index(arr)
    mx = 0

    for i, j, k in zip(left, right, range(len(arr))):
        temp = (j - i - 1) * arr[k]
        mx = max(mx, temp)

    return mx


# print(HistogramArea([6, 2, 5, 4, 5, 1, 6]))

matrix = [[0, 1, 1, 0],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 0, 0]]


def AreaBinaryMat(mat):
    temp_mat = [0 for i in range(len(mat[0]))]
    mx = 0

    for i in range(len(mat)):

        for j in range(len(mat[0])):

            if mat[i][j] == 0:
                temp_mat[j] = 0

            else:
                temp_mat[j] = temp_mat[j] + 1

        mx = max(mx, HistogramArea(temp_mat))

    return mx


# print(AreaBinaryMat(matrix))


def Rainwater(arr):
    water = 0

    for i in range(1, len(arr) - 1):
        temp_left = max(arr[:i])
        temp_right = max(arr[i + 1:])

        water += min(temp_left, temp_right) - arr[i]

    return water


w = [3, 0, 0, 2, 0, 4]

# print(Rainwater(w))
