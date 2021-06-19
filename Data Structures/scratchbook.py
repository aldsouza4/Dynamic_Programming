from collections import defaultdict

class Solution:
    def isPossible(self, N, prerequisites):
        self.dependencyEdges = defaultdict(list)

        for x, y in prerequisites:
            self.dependencyEdges[x].append(y)

        self.canFinish = [False] * (N+1)

        for v in range(1, N + 1):
            res =