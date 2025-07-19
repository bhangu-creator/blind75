class Solution:
    # Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V, adj):
        
        def find(u, parent):
            if parent[u] != u:
                parent[u] = find(parent[u], parent)
            return parent[u]
        
        def union(u, v, parent, rank):
            pu, pv = find(u, parent), find(v, parent)
            if pu == pv:
                return
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pu] += 1
        
        parent = [i for i in range(V)]
        rank = [0] * V
        
        for u in range(V):
            for v in adj[u]:
                if u < v:  # Avoid double-processing undirected edges
                    if find(u, parent) == find(v, parent):
                        return 1  # Cycle detected
                    union(u, v, parent, rank)
        
        return 0  # No cycle found
