from collections import defaultdict

#


class Graph:

    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        self.num_vertices = num_vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def iscyclicutil(self, node, visited, stack):
        visited[node] = True
        stack[node] = True

        for neighbour in self.graph[node]:
            if not visited[neighbour]:
                if self.iscyclicutil(neighbour, visited, stack):
                    return True
            elif stack[neighbour]:
                return True

        stack[node] = False
        return False

    def iscyclic(self):
        visisted = [False] * (self.num_vertices + 1)
        stack = [False] * (self.num_vertices + 1)

        for node in range(self.num_vertices):
            if not visisted[node]:
                if self.iscyclicutil(node, visisted, stack):
                    return True

        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

if g.iscyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")
