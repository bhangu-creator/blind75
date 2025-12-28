#we had to identify which cells marked as O cannot espace the matrix, here escaping meant cannot reach the boudary
#so we did a loop over the edges of the matrix and using dfs went to each connected region and marked it in dummy matrix 
#in end did a loop over dummy matrix whichever coords were not visited means they are the one's who cannot explain so assigned them X

#time complexity due to dfs - O(m*n) and space is also O(m*n)

from typing import List;

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Row=len(board)
        Col=len(board[0])

        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        visited= [[False for _ in range(Col)] for row in range(Row) ]

        def dfs(row,col):
            if not visited[row][col]:
                visited[row][col]=True
                for x,y in directions:
                    rx=x+row
                    ry=y+col
                    if rx>=0 and rx<Row and ry>=0 and ry<Col and board[rx][ry]=="O":
                        dfs(rx,ry)

        col=0
        for row in range(Row):
            if board[row][col]=="O":
                dfs(row,col)
        row=0
        for col in range(Col):
            if board[row][col]=="O":
                dfs(row,col)

        col=Col-1
        for row in range(Row):
            if board[row][col]=="O":
                dfs(row,col)

        row=Row-1
        for col in range(Col):
            if board[row][col]=="O":
                dfs(row,col)


        for row in range(Row):
            for col in range(Col):
                if not visited[row][col] and not visited[row][col]:
                    board[row][col]="X"
        
