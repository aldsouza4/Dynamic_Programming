def minimumPlatform(arr, dep):
    if len(arr) == 0 or len(dep) == 0:
        return 0

    arr = [float(x) for x in arr]
    dep = [float(x) for x in dep]
    dep.sort()

    ans = 0

    i = 1
    j = 0

    queue = [arr[0]]

    while i < len(arr):

        while i < len(arr) and arr[i] < dep[j]:
            queue.append(arr[i])
            ans = max(len(queue), ans)
            i += 1

        queue.pop(0)
        j += 1

    return ans


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

# arr = [900, 1100, 1235]
# dep = [1000, 1200, 1240]

# arr = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
# dep = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]

print(minimumPlatform(arr, dep))

