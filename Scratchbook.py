# print an arraygreater to the right
x = [1, 3, 2, 4]
# op : [3, 4, 4, -1]

def NGR(arr):
    resArry = []
    stack = []

    for i in range(len(arr)-1, -1, -1):
        if len(stack) == 0:
            resArry.append(-1)

        else:
            if stack[-1] > arr[i]:
                resArry.append(stack[-1])

            elif stack[-1] < arr[i]:
                while len(stack)>0 and stack[-1] < arr[i]:
                    stack.pop()

                if len(stack) == 0:
                    resArry.append(-1)

                else:
                    resArry.append(stack[-1])

        stack.append(arr[i])

    return resArry[::-1]


print(NGR(x))