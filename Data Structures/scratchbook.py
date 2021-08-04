from collections import defaultdict


class Solution:
    def isCircle(self, n, strs):
        if n == 0:
            return

        return self.makegraph(strs)

    def makegraph(self, strings):
        graph = defaultdict(list)

        for i in strings:
            graph[i[0]].append(i[-1])

        return graph


