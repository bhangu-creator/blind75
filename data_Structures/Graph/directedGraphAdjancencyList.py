from collections import defaultdict
from collections import deque

class directGraphList:       

    def build_list(self,n):
        adj=[[] for _ in range(n)]
        self.vis=[False]*n
        return adj
    
    def add_edge(self,adj,i,j):
        adj[i].append(j)
    def remove_edge(self,adj,i,j):
        adj[i].remove(j)

    def add_vertex(self,adj):
        adj.append([])

    def remove_vertex(self,adj,u):
        adj.pop(u)
        for ver in range(len(adj)):
            newList=[]
            for vert in adj[ver]:
                if u==vert:
                    continue
                elif vert>u:
                    newList.append(vert-1)
                else:
                    newList.append(vert)
            adj[ver]=newList

    def dfs_iterative(self,adj,start):
        visited=[False] * len(adj)
        stack=[start]
        while stack:
            node=stack.pop()
            if not visited[node]:
                visited[node]=True
                for neighbours in reversed(adj[node]):
                    if not visited[neighbours]:
                        stack.append(neighbours)
        return visited
    
    def dfs_recursive(self,adj,start):
        if not self.vis[start]:
            self.vis[start]=True
            for neighbours in adj[start]:
                if not self.vis[neighbours]:
                    self.vis[neighbours]=True
                    self.dfs_recursive(adj,neighbours)
        else: 
            return
    def dfs_disconnected_iterative(self,adj):
        vis=[False]*len(adj)
        stack=[]
        for node in range(len(adj)):
            if not vis[node]:
                stack.append(node)
                while stack:
                    vertex=stack.pop()
                    if not vis[vertex]:
                        vis[vertex]=True
                        for neighbours in reversed(adj[vertex]):
                            if not vis[neighbours]:
                                stack.append(neighbours)
    def dfs_disconnected_recursive(self,adj):
        def dfs(node):
            self.vis[node]=True
            for neighbour in adj[node]:
                if not self.vis[neighbour]:
                    self.dfs(neighbour)

        for node in range(len(adj)):
            if not self.vis[node]:
                dfs(node)
            
    def bfs_connected(self,adj,start):
        vis=[False] * len(adj)
        queue=deque()
        queue.append(start)
        vis[start]=True
        while queue:
            node=queue.popleft()
            for neighbours in adj[node]:
                if not adj[neighbours]:
                    queue.append(neighbours)
                    vis[neighbours]=True
                    
    def bfs_disconnected(self,adj):
        vis=[False] * len(adj)
        queue=deque()
        for node in range(len(adj)):
            if not vis[node]:
                queue.append(node)
                vis[node]=True
                while queue:
                    vertex=queue.popleft()
                    for neighbours in adj[vertex]:
                        if not vis[neighbours]:
                            queue.append(neighbours)
                            vis[neighbours]=True

            

    def isConnected(self,vis=None):
        if vis==None:
            return all(self.vis)
        else:
            return all(vis)

    def display_list(self,adj):
        for i in range(len(adj)):
            print(f"{i}:",end="")
            for j in adj[i]:
                print(j,end=" ")
            print()

sol=directGraphList()
adj=sol.build_list(3)
sol.add_edge(adj,1,0)
sol.add_edge(adj,1,2)
sol.add_edge(adj,2,0)
sol.remove_edge(adj,1,0)
#sol.remove_vertex(adj,0)
vis=sol.dfs_iterative(adj,0)
sol.dfs_recursive(adj,0)
con=sol.isConnected(vis)
con1=sol.isConnected()
print(con)
print(con1)
sol.display_list(adj)