#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    
    
    #this problem is solved using iterative DFS 
    #the intuation for this problem is it is very similar to the no of islands problem.. we know that we can use DFS to see how many islands are there means that how many coords are there that are "1" , we know that an islad is 1 island when all the 1's are adjacently connected up and down and the water is around them
    #now in this problem we needed to find no of distinct islands, which basically means island that are not identical in shape.... 
    #the most important point to understand about this problem is that how to get an island shape? from every coordinate where we start the DFS before that we can say the starting coords as our base x and base y, all the rest of the islands that are connected to the base x and base y will be computed using relative coords and will be stored as list of tuples in a set
    #since this problem require distinct results we are using a set that way all the duplicate relative coords will get cancel out leaving only distict islands relative coords
    def __init__(self): #initialzing the x and y vectors for DFS
        self.dx=[1,0,-1,0]
        self.dy=[0,1,0,-1]
    
    def isValid(self,row,col,grid):
        if row<0 or col<0 or row>=self.rows or col>=self.cols:
            return False
        elif grid[row][col]==7 or grid[row][col]==0:
            return False
        else:
            return True
        
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        dist=set()
        self.rows=len(grid)
        self.cols=len(grid[0])
        st=[]
        for row in range(self.rows):          #using DFS to navigate to all possible connected islands
            for col in range(self.cols):
                if grid[row][col] != 7 and grid[row][col] == 1:
                    base_row, base_col = row, col             #relative coords initialization
                    distinctList=[]                          #initialzing a list to store tuples
                    st.append([row,col])
                    while st:
                        rrow,coll=st.pop()
                        if self.isValid(rrow,coll,grid):
                            grid[rrow][coll]=7
                            distinctList.append((base_row-rrow,base_col-coll))   #computing the relative coords of all the connected islands and storing them in list
                            for i in range(4):
                                adjx=rrow+self.dx[i]
                                adjy=coll+self.dy[i]
                                st.append([adjx,adjy])
                    dist.add(tuple(distinctList))  #adding the list to set by first converting it to a tuple, since list are not hashable 
        return len(dist) #returning the no of distinct islands
    
sol=Solution()
grid = [
  [1, 1, 0, 1],
  [1, 0, 0, 1],
  [0, 0, 0, 1]
]
val=sol.countDistinctIslands(grid)
print(val)