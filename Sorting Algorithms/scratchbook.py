from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.num_vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def topologicalsortutil(self, vertex, visited, stack):
        visited[vertex] = True

        for i in self.graph[vertex]:
            if not visited[i]:
                self.topologicalsortutil(i, visited, stack)

        stack.append(vertex)


    def topologicalSort(self):

        visited = [False]*self.num_vertices
        stack = []

        for i in range(self.num_vertices):
            if not visited[i]:
                self.topologicalsortutil(i, visited, stack)

        print(stack[::-1])


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)


#
print("Following is a Topological Sort of the given graph")

# Function Call
g.topologicalSort()




