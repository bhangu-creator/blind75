from typing import List
from collections import defaultdict
from collections import deque

class Solution:

    #same as finding a cycle in graph, in this case if we found a cycle return False as we cannot finish all the courses in that case
    def canFinish_dfs_recur(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)
        visited=[False]* numCourses
        recurStack=[False]* numCourses
        def dfs(node):
            visited[node]=True
            recurStack[node]=True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if not dfs(neighbor):
                        return False
                elif recurStack[neighbor]:
                    return False
            recurStack[node]=False
            return True
        for ver in range(numCourses):
            if not visited[ver]:
                if not dfs(ver):
                    return False
        return True
    

    #using kahn's algo for bfs topological sort (indegree logic)
    #intuation is if all the degree's of the nodes of graph can be reduced to zero that means that it is not a cycle
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        indegree=[0] * numCourses
        count=0
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        queue=deque()
        for ver in range(numCourses):
            if indegree[ver]==0:
                queue.append(ver)
                count+=1
        while queue:
            vertex=queue.popleft()
            for neighbor in adj[vertex]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
                    count+=1
        if count==numCourses:
            return True
        else:
            return False



