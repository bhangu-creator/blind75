from typing import List
from collections import defaultdict
from collections import deque

class Solution:

    #this problems requires finding topo sort, since there can be a cycle in the graph we first check that and then return teh toposort using dfs
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited=[False] * numCourses
        recurStack=[False] * numCourses
        adj=defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)
        isCycleBol=False
        def isCycle(node):
            if not visited[node]:
                visited[node]=True
                recurStack[node]=True
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        if isCycle(neighbor):
                            return True
                    elif recurStack[neighbor]:
                        return True
                recurStack[node]=False
                return False
        for ver in range(numCourses):
            if not visited[ver]:
                if isCycle(ver):
                    return []
        returStack=[]
        visited=[False] * numCourses
        def dfs(node):
            if not visited[node]:
                visited[node]=True
                for neighbor in adj[node]:
                    dfs(neighbor)
                returStack.append(node)
        for ver in range(numCourses):
            if not visited[ver]:
                dfs(ver)
        return returStack[::-1]


    #kahn's algo for bfs to find toposort and find out circle in graph
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indegree=[0] * numCourses
        count=0
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        queue=deque()
        stack=[]
        for deg in range(len(indegree)):
            if indegree[deg]==0:
                count+=1
                queue.append(deg)
        while queue:
            node=queue.popleft()
            stack.append(node)
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    count+=1
                    queue.append(neighbor)
        if count==numCourses:
            return stack
        else:
            return []        


        

        