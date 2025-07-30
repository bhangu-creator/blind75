from typing import List
import heapq

class Solution:
    def __init__(self):
        self.dx=[-1,1,0,0,-1,-1,1,1]
        self.dy=[0,0,-1,1,-1,1,-1,1]
        
    def isVisited(self,row,col,visited,grid):
        if row<0 or col<0 or row>=self.Row or col>=self.Col or grid[row][col]==1 or visited[row][col]:
            return False
        return True
                
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        queue=[]
        heapq.heappush(queue,(0,0,0))
        self.Col=self.Row=n
        distance=[[float('inf') for _ in range(n)] for _ in range(n)]
        distance[0][0]=0
        visited=[ [False for _ in range(n)]for _ in range(n)]
        while queue:
            curr_dist,curr_x,curr_y=heapq.heappop(queue)
            if self.isVisited(curr_x,curr_y,visited,grid):
                visited[curr_x][curr_y]=True
                for i in range(8):
                    dx=curr_x+self.dx[i]
                    dy=curr_y+self.dy[i]
                    if self.isVisited(dx,dy,visited,grid):
                        if distance[dx][dy]>1+curr_dist:
                            distance[dx][dy]=1+curr_dist
                            heapq.heappush(queue,(distance[dx][dy],dx,dy))
        if visited[n-1][n-1]:
            return (distance[n-1][n-1] + 1)
        else:
            return -1