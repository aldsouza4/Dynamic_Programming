def negativewindow(arr, win):
    i = 0
    j = 0
    neg_list = []
    resArray = []

    while j < len(arr):
        if arr[j] < 0:
            neg_list.append(arr[j])

        if j - i + 1 < win:
            j += 1

        elif j - i + 1 == win:
            if len(neg_list) == 0:
                resArray.append(0)

            else:
                resArray.append(neg_list[0])

            if len(neg_list) > 0 and neg_list[0] == arr[i]:
                neg_list = neg_list[1:]

            i += 1
            j += 1

    return resArray


# vector = [12, -1, -7, 8, -15, 30, 16, 28]
# print(negativewindow(vector, 3))

def anagram(arr, check):

    arr = list(arr)
    check = list(check)
    ans = 0

    map = {}
    for i in check:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    count = len(map)
    i = 0
    j = 0

    while j < len(arr):

        if arr[j] in map:
            map[arr[j]] -= 1

            if map.get(arr[j]) == 0:
                count -= 1



        if j - i + 1 == len(check):
            if count == 0:
                ans += 1

            if arr[i] in map:
                map[arr[i]] += 1

            if map.get(arr[i]) == 1:
                count += 1

            i += 1
            j += 1

        if j - i + 1 < len(check):
            j += 1

    return ans


# print(anagram("ABCHJTABCCBAABCDHDJSJ", "ABC"))


def maxinWindows(arr, k):


