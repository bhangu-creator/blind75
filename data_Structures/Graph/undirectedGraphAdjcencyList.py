from collections import defaultdict


class undirectGraph:
    def build_list(self):
        adj=defaultdict(list)
        return adj
    def add_edge(self,adj,i,j):
        adj[i].append(j)
        adj[j].append(i)
    def display_list(self,adj):
        for ver1,ver2 in adj.items():
            print(f"{ver1}:"," ".join(map(str,ver2)))

sol=undirectGraph()
adj=sol.build_list()
sol.add_edge(adj,0,1)
sol.add_edge(adj,0,2)
sol.add_edge(adj,1,2)
sol.add_edge(adj,2,3)
sol.display_list(adj)