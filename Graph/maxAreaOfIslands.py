from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Row=len(grid)
        Col=len(grid[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        visited=[[False for _ in range(Col)] for _ in range(Row)]

        def isValid(row,col):
            if row<0 or row>=Row or col<0 or col>=Col or visited[row][col] or grid[row][col]==0:
                return False
            return True

        def dfs(row,col):
            self.noOfIsalnds+=1
            visited[row][col]=True
            for x,y in directions:
                adjx=row+x
                adjy=col+y
                if isValid(adjx,adjy):
                    dfs(adjx,adjy)

        self.noOfIsalnds=0
        maxArea=0
        for row in range(Row):
            for col in range(Col):
                if isValid(row,col,):
                    dfs(row,col)
                    maxArea=max(maxArea,self.noOfIsalnds)
                    self.noOfIsalnds=0
        return maxArea

#just count no of islands and return the max
