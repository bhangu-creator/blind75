from typing import List
from collections import deque

class Solution:
    
    #this problem can be solved using DFS and BFS for 2d arrays
    #the first approach is DFS iterative approach
    
    def __init__(self):        #this is constructor used to initialize the direction vectors for the DFS search, when we start at any coordinate for ex (0,0) we will check the next coordinate to go to check in all 4 directions left,right,top,bottom 
        self.dx=[0,1,0,-1]    #this is x coordinate directions 
        self.dy=[1,0,-1,0]    #this is y coordinate directions
        
    def isValid(self,row,col,grid):   #this is a method which we will use to check if we have visisted the coordinates before or if the coordinates we are on are in range and are valid
        
        if row<0 or col<0 or row>=self.Row or col>=self.Col:  #this condition will check if the coordinates we are on are valid and are inside the 2d matrix
            return False
        if self.vis[row][col] or grid[row][col]=='0':      #this condition will check if we have visisted the coordinates before and if the coordinates that we are on is "island" or not meaning it's value is 1 or not , if it is 0 then return false
            return False
        else:
            return True
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.Row=len(grid)       #here we have got the row length of the given matrix
        self.Col=len(grid[0])    #here we have got the column length of the given matrix
        self.vis = [[False for _ in range(self.Col)] for _ in range(self.Row)]     #here we have created a new 2d array matrix of equal size as given matrix and just initialized all the rows and colums as False as we have not visited any of them yet
        count=0    #this will keep count of how much island are there effectively keeping the count how much deep DFS can go without breaking
        st=[]      #initializing stack to store the coordinates to backtrack
        
        for rows in range(0,self.Row):      #these two loops will traverse the whole matrix for each row,column to check how many island are there
            for cols in range(0,self.Col):
                if not self.vis[rows][cols] and grid[rows][cols] == '1':     #this is condition to make the code more optimal , it will skip the check for the coordinates which are not islands and which are already visited
                    count+=1       #if the control came in this if that would definitely mean that we have atleast 1 island found so increase the count here
                    st.append([rows, cols])     #put the first coordinates in the stack
                    while len(st)>0:            #starts the while loop for the coordinates in the stacks
                        row,col=st.pop()        #popped the top most element of stack and then assign them to row and col
                        if not self.isValid(row,col,grid):   #check if they are valid coordinates means they are not visisted yet
                            continue
                        else:
                            self.vis[row][col]=True    #if not then just mark them True
                        for i in range(4):              #now this is the most important part of DFS , this loop will store all the coordinates in all 4 direction of the given coordinate
                            adjx=row+self.dx[i]
                            adjy=col+self.dy[i]
                            st.append([adjx,adjy])   #all the 4 coordinate will then put into stack to check for further until the stack become empty means we reached the end of our DFS search and have checked all possible connnected islands
        return count  #return the count of island for each coordiante
    
    
    #now lets do the same DFS for this problem using recursion
    
    def dfsRecur(self,coord,grid):
        row=coord[0]
        col=coord[1]
        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col]=='0': #base condition
            return 
        if grid[row][col]=='$':   #base condition II
            return 
        else:
            grid[row][col]='$'   #marking every coords as $ when visited
            for i in range(4):
                adjx=row+self.dx[i]
                adjy=col+self.dy[i]
                self.dfsRecur([adjx,adjy],grid)
            
        
    
    def numsOfIslandDfsRecur(self, grid: List[List[str]]) -> int:
        count=0
        for rows in range(0,len(grid)):      #these two loops will traverse the whole matrix for each row,column to check how many island are there
            for cols in range(0,len(grid[0])): 
                if grid[rows][cols]=='1':   #only run loop when coord value is 1
                    count+=1     #increase the count only when dfs is called for a coord
                    self.dfsRecur([rows,cols],grid)
        return count
         
         
                    
    
    #now lets use BFS for this problem using queue
    #the only difference in BFS and DFS here is that we are using queue here and also is that we first verify if the coords are valid then we append them in the queue and then we mark them visited    
        
    def isValidBFS(self,row,col,grid):   #this is a method which we will use to check if we have visisted the coordinates before or if the coordinates we are on are in range and are valid
        
        if row<0 or col<0 or row>=self.Row or col>=self.Col:  #this condition will check if the coordinates we are on are valid and are inside the 2d matrix
            return False
        if grid[row][col]=="$" or grid[row][col]=='0':      #this condition will check if we have visisted the coordinates before and if the coordinates that we are on is "island" or not meaning it's value is 1 or not , if it is 0 then return false
            return False
        else:
            return True
        
        
    def numsOfIslandBFS(self, grid: List[List[str]]) -> int:
        self.Row=len(grid)
        self.Col=len(grid[0])
        islandCount=0
        for rows in range(self.Row):      #these two loops will traverse the whole matrix for each row,column to check how many island are there
            for cols in range(self.Col):
                q=deque()
                if self.isValidBFS(rows,cols,grid):  #check if the coords are valid , if yes than apply the BFS on them
                    q.append([rows,cols])  #append the valid coords
                    grid[rows][cols]="$"  #mark the coords visited
                    while q:  
                        row,col=q.popleft()
                        for i in range(4):
                            adjx=row+self.dx[i]
                            adjy=col+self.dy[i]
                            if self.isValidBFS(adjx,adjy,grid):
                                q.append([adjx,adjy])   #append the valid coords
                                grid[adjx][adjy]="$"  #mark the coords visited
                    islandCount+=1                
            
        return islandCount            
                 
sol=Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
val=sol.numsOfIslandBFS(grid)
print(val)












