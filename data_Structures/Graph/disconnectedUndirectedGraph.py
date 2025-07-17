# Python3 implementation for DFS on a disconnected, undirected graph using adjacency matrix
class Graph:
    
    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.adj = [[0 for _ in range(v)] for _ in range(v)]

    def addEdge(self, u, v):
        # Undirected graph
        self.adj[u][v] = 1
        self.adj[v][u] = 1

    def DFS(self, node, visited):
        print(node, end=' ')
        visited[node] = True
        for neighbor in range(self.v):
            if self.adj[node][neighbor] == 1 and not visited[neighbor]:
                self.DFS(neighbor, visited)

# Example usage
v, e = 5, 4
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(3, 4)  # Disconnected component
G.addEdge(2, 3)  # Now connects component

visited = [False] * v

# Handle disconnected components
for i in range(v):
    if not visited[i]:
        G.DFS(i, visited)
        print()  # Optional: separate components
