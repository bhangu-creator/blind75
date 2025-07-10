from collections import defaultdict


class directGraphList:
    def build_list(self,n):
        adj=[[] for _ in range(n)]
        return adj
    def add_edge(self,adj,i,j,w):
        adj[i].append((j,w))
    def display_list(self,adj):
        for i in range(len(adj)):
            print(f"{i}:",end="")
            for j in adj[i]:
                print(j,end=" ")
            print()

sol=directGraphList()
adj=sol.build_list(3)
sol.add_edge(adj,1,0,4)
sol.add_edge(adj,1,2,3)
sol.add_edge(adj,2,0,1)
sol.display_list(adj)