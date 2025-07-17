from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False] * n
        def dfs(node,visited):
            visited[node]=True
            for neighbor in range(n):
                if isConnected[node][neighbor]==1 and visited[neighbor]==False:
                    dfs(neighbor,visited)
        provisions=0
        for ver in range(n):
            if not visited[ver]:
                provisions+=1
                dfs(ver,visited)
        
        return provisions

#using bfs
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False] * n
        def bfs(node,visited):
            queue=deque()
            queue.append(node)
            while queue:
                vertex=queue.popleft()
                if not visited[vertex]:
                    visited[vertex]=True
                    for neighbor in range(n):
                        if isConnected[vertex][neighbor]==1 and not visited[neighbor]:
                            queue.append(neighbor)
        provisions=0
        for ver in range(n):
            if not visited[ver]:
                provisions+=1
                bfs(ver,visited)
        
        return provisions


        



