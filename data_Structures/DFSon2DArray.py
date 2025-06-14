class Solution:
    
    def __init__(self):
        self.ROW=3
        self.COL=3
        # Initialize direction vectors
        self.dRow= [0, 1, 0, -1]
        self.dCol=[1, 0, -1, 0]
        self.vis=[[False for i in range(3)] for j in range(3)]
    
  # Function to check if mat[row][col]  is unvisited and lies within the boundary of the given matrix
    def isValid(self,row,col)->bool:
        
        #if cell is out of bounds
        if row<0 or col<0 or row>=self.ROW or col>=self.COL:
            return False
        
        #check if the cell is visited before
        if self.vis[row][col]:
            return False
        else:
            return True
        
    #function to perform DFS on 2d Array
    def DFS(self,row,col,grid):
        
        #initialize a stack of pair and push a starting pair into it
        st=[]
        st.append([row,col])
        
        #iterate until the stack is not empty
        while len(st)>0:
            #pop the top pair
            curr=st[len(st)-1]
            st.remove(st[len(st)-1])
            row=curr[0]
            col=curr[1]
            #check if the current popped cell is visited or not
            if not self.isValid(row,col):
                continue
            
            #mark the current cell as True/visited
            self.vis[row][col] = True
            
            # Print the element at  the current top cell
            print(grid[row][col], end = " ")
            
            #push all the adjacent cells in stack
            for i in range(4):
                adjx=row+self.dRow[i]
                adjy=col+self.dCol[i]
                st.append([adjx,adjy])
                
sol=Solution()
grid =  [[-1, 2, 3],
             [0, 9, 8],
             [1, 0, 1]]
sol.DFS(0,0,grid)
                
        
        
        
