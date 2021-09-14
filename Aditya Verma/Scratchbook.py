# Given an array arr[] of size N and an integer K. Find the maximum for
# each and every contiguous subarray of size K.

# Input : 'forxxorfxdofr'
# Pattern: 'for'
# Output : 3


def countoccurances(text: str, pat: str):
    text = list(text)
    pat = list(pat)
    n = len(text)
    m = len(pat)

    map = {}
    for i in pat:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1

    count = len(map)

    i, j, ans = 0, 0, 0

    while j < n:

        if j - i + 1 <= m:
            if text[j] in map:
                map[text[j]] -= 1

                if map[text[j]] == 0:
                    count -= 1

        if j - i + 1 == m:
            if count == 0:
                ans += 1

            if text[i] in map:
                map[text[i]] += 1

                if map[text[i]] == 1:
                    count += 1

            i += 1

        j += 1

    return ans


print(countoccurances('aabaabaa', 'aaba'))
