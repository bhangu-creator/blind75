from collections import defaultdict
from collections import deque
class Solution:

    #intuation is that first:
    #graph can be connected or disconnected so we have to use dfs on all nodes so for that we use for loop on all the available edges
    #then in problems like these there are always connection given like connection bw two edges so we have to create an adc list from those connections
    #now we also have to maintain a global vis to verify if the node has already been visited and cleared
    #also we will store the parent with each node so that we can verify it for cycle, using cycle we can only go to unvisited line and if we did go to previosuly visisted nodes and the we can verify if that node is the parent of our curr node if not then that means there is a cycle
    #concept is very simple that we can only go straight.. but if somehow we ended upon already visited node and it is not our parent node that means it is a cycle
    def isCycle(self, V, edges):
        adj = defaultdict(list)
        for v, u in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = [False] * V

        def dfs(node):
            stack = []
            stack.append((node, -1))
            while stack:
                vertex, parent = stack.pop()
                if vis[vertex]:
                    continue
                vis[vertex] = True
                for neighbor in adj[vertex]:
                    if not vis[neighbor]:
                        stack.append((neighbor, vertex))
                    elif neighbor != parent:
                        return True
            return False

        for i in range(V):
            if not vis[i]:
                if dfs(i):
                    return True
        return False


    def isCycle_recur(self, V, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * V

        def dfs(start, parent):
            vis[start] = True
            for neighbor in adj[start]:
                if not vis[neighbor]:
                    if dfs(neighbor, start):    #core logic, explore all the branches and if found a cycle just return True
                        return True
                elif neighbor != parent:
                    return True
            return False

        for node in range(V):
            if not vis[node]:
                if dfs(node, -1):
                    return True
        return False

    def isCycle_BFS(self, V, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * V

        def bfs(start):
            queue = deque()
            queue.append((start, -1))
            while queue:
                vertex, parent = queue.popleft()
                if not vis[vertex]:
                    vis[vertex] = True
                    for neighbor in adj[vertex]:
                        if not vis[neighbor]:
                            queue.append((neighbor, vertex))
                        elif neighbor != parent:
                            return True
            return False

        for node in range(V):
            if not vis[node]:
                if bfs(node):
                    return True
        return False


sol=Solution()
bol=sol.isCycle(6,[[0,1],[1,2],[1,3],[2,4],[3,4],[4,5]])
print(bol)