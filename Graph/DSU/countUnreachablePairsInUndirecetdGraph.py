from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        def find(u,parent):
            if u==parent[u]:
                return u
            parent[u]=find(parent[u],parent)
            return parent[u]

        def union(u,v,parent,rank):
            par_u=find(u,parent)
            par_v=find(v,parent)
            if par_u==par_v:
                return
            if rank[par_u]>rank[par_v]:
                parent[par_v]=par_u
            elif rank[par_u]<rank[par_v]:
                parent[par_u]=par_v
            else:
                parent[par_u]=par_v
                rank[par_v]+=1

        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent=[i for i in range(n)]
        rank=[0] * n
        for ver in range(n):
            for node in adj[ver]:
                if ver<node:
                    union(ver,node,parent,rank)
        unreached={}
        for ver in range(n):
            par=find(ver,parent)
            if par not in unreached:
                unreached[par]=1
            else:
                unreached[par]+=1
        result=0
        prev=0
        for par,count in unreached.items():
            size=count
            remaining=n-prev
            result+=size * (remaining-size)
            prev+=size
        return result

sol=Solution()
res=sol.countPairs(7,[[0,2],[0,5],[2,4],[1,6],[5,4]])
print(res)


        