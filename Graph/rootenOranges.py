class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Row,Col=len(grid),len(grid[0])
        rotten= [[False for _ in range(Col)] for _ in range(Row)]
        queue=deque()
        for row in range(Row):
            for col in range(Col):
                if grid[row][col]==2:
                    rotten[row][col]=True
                    queue.append((row,col))
                             
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        time=0
        while queue:
            for _ in range(len(queue)):
                row,col=queue.popleft()
                for rx,ry in directions:
                    adjx=rx+row
                    adjy=ry+col
                    if adjx>=0 and adjx<Row and adjy>=0 and adjy<Col and not rotten[adjx][adjy] and grid[adjx][adjy]==1:
                        rotten[adjx][adjy]=True
                        queue.append((adjx,adjy))
            time+=1
        
        for row in range(Row):
            for col in range(Col):
                if grid[row][col]==1 and not rotten[row][col]:
                    return -1
        return time-1 if time>1 else 0



        

