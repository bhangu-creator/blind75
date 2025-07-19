from typing import List
from collections import defaultdict

class Solution:

    #used the dfs on undirected disconnected graph to count the unconected clusters than just returned that number with -1
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        adj=defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        visited= [False] * n
        diconnectedNetworks=0
        def dfs(node):
            visited[node]=True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        for ver in range(n):
            if not visited[ver]:
                diconnectedNetworks+=1
                dfs(ver)
        return diconnectedNetworks-1

    #using union find:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        def find(a,parent):
            if a==parent[a]:
                return a
            parent[a]=find(parent[a],parent)
            return parent[a]

        def union(a,b,parent,rank):
            a_par=find(a,parent)
            b_par=find(b,parent)
            if a_par==b_par:
                return
            if rank[a_par]>rank[b_par]:
                parent[b_par]=a_par
            elif rank[a_par]<rank[b_par]:
                parent[a_par]=b_par
            else:
                parent[b_par]=a_par
                rank[a_par]+=1
        parent=[i for i in range(n)]
        rank=[0] * n
        for u,v in connections:
            union(u,v,parent,rank)
        clusters=set()
        for vertex in range(len(parent)):
            clusters.add(find(vertex,parent))
        return len(clusters)-1




