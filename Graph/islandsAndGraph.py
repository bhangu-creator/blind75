from typing import List
import heapq
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        heap=[]
        Row=len(grid)
        Col=len(grid[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        for row in range(Row):
            for col in range(Col):
                if grid[row][col]==0:
                    heapq.heappush(heap,(0,(row,col)))
        while heap:
            curr_dist,coords=heapq.heappop(heap)
            row,col=coords
            if curr_dist>grid[row][col]:
                continue
            new_dist=curr_dist+1
            for x,y in directions:
                adjx=row+x
                adjy=col+y
                if adjx>=0 and adjx<Row and adjy>=0 and adjy<Col and grid[adjx][adjy]!=-1 and grid[adjx][adjy]!=0:
                    if grid[adjx][adjy]>new_dist:
                        grid[adjx][adjy]=new_dist
                        heapq.heappush(heap,(new_dist,(adjx,adjy)))

#just read dijkstra algorithm,pretty simple situation for this time is O(m*n)*log(m*n) and space is o(m*n)

#now if cases where the graph is unweighted or all the edges has same weight like the one here then use bfs simply
#then the time and space both will be o(m*n)

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque()
        Row=len(grid)
        Col=len(grid[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        for row in range(Row):
            for col in range(Col):
                if grid[row][col]==0:
                    queue.append((0,(row,col)))
        while queue:
            curr_dist,coords=queue.popleft()
            row,col=coords
            new_dist=curr_dist+1
            for x,y in directions:
                adjx=row+x
                adjy=col+y
                if adjx>=0 and adjx<Row and adjy>=0 and adjy<Col and grid[adjx][adjy]!=-1 and grid[adjx][adjy]!=0:
                    if grid[adjx][adjy]>new_dist:
                        grid[adjx][adjy]=new_dist
                        queue.append((new_dist,(adjx,adjy)))


