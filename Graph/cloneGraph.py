from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    #the intuation is very simple use any traversal method to traverse the grapha and at each vertex clone the vertex itself and the neighbors also

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited={}
        def dfs(node):
            newNode=Node(node.val)
            if node.val not in self.visited:
                self.visited[node.val]=newNode
                for neighbor in node.neighbors:
                    newNode.neighbors.append(dfs(neighbor))
            return self.visited[node.val]
        if node is None:
            return None
        return dfs(node)
    
    #same solution using dfs iterative , the intuationis using hashmap to store the cloned node as value to the original node which act as key

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        stack=[]
        visited={}
        visited[node]=Node(node.val)
        stack.append(node)
        while stack:
            curr=stack.pop()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor]=Node(neighbor.val)
                    stack.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]
    
    #same as dfs iterative just used queue here, since it is BFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        queue=deque()
        visited={}
        visited[node]=Node(node.val)
        queue.append(node)
        while queue:
            curr=queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor]=Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]


        