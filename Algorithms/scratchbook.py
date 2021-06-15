from collections import defaultdict


class Solution:
    def dfs(self, v, visited):
        if self.canFinish[v]:
            return 1

        if v in visited:
            return 0

        visited.add(v)
        for neighbor in self.dependencyEdges[v]:
            res = self.dfs(neighbor, visited)
            if not res:
                return res
        visited.remove(v)
        return 1

    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        self.dependencyEdges = defaultdict(list)
        for (x, y) in zip(B, C):
            self.dependencyEdges[y].append(x)

        self.canFinish = [False] * (A + 1)

        for v in range(1, A + 1):
            res = self.dfs(v, set([]))
            if not res:
                return 0

            self.canFinish[v] = True

        return 1