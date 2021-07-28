class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)]
                      for row in range(V)]

    # This function returns true if graph G[V][V]
    # is Bipartite, else false
    def isBipartiteUtil(self, src):

        # Create a color array to store colors
        # assigned to all veritces. Vertex
        # number is used as index in this array.
        # The value '-1' of self.colorArr[i] is used
        # to indicate that no color is assigned to
        # vertex 'i'. The value 1 is used to indicate
        # first color is assigned and value 0
        # indicates second color is assigned.

        # Assign first color to source

        # Create a queue (FIFO) of vertex numbers and
        # enqueue source vertex for BFS traversal
        queue = [src]
        self.colorArr[src] = 1

        # Run while there are vertices in queue
        # (Similar to BFS)
        while queue:

            u = queue.pop(0)

            # Return false if there is a self-loop
            # if self.graph[u][u] == 1:
            #     return False

            for v in self.graph[u]:

                # An edge from u to v exists and
                # destination v is not colored
                if self.colorArr[v] == -1:
                    self.colorArr[v] = (1 - self.colorArr[u])
                    queue.append(v)

                else:
                    if self.colorArr[v] == self.colorArr[u]:
                        return False

        # If we reach here, then all adjacent
        # vertices can be colored with alternate
        # color
        return True

    def isBipartite(self):
        self.colorArr = [-1 for i in range(self.V)]

        for i in range(self.V):
            if self.colorArr[i] == -1:
                if not self.isBipartiteUtil(i):
                    return False
        return True


g = Graph(4)
g.graph = [[1, 3], [0, 2], [1, 3], [0, 2]]

print("Yes" if g.isBipartite() else "No")
