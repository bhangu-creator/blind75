from typing import List

class Solution:
    
    #the intuation is simple, we know if the rain falls on any of the cells they  overflow and the water goes to neughbouring cells and eventualy to either of the ocean, we need coords of the cells from which when water overflows it goes to both the ocean
    #first lets start from 1 ocean edge cells and backtrack to see where can the water come from , mark all the cells as for  pacific and store their cords in a set
    #do the same for the 2nd ocean edge cells and mark it for Atlantic and store there coords in a different set also
    #get the intersection of both of these sets and you will have common cells who share the water from both the oceans
        
        def __init__(self):        #this is constructor used to initialize the direction vectors for the DFS search, when we start at any coordinate for ex (0,0) we will check the next coordinate to go to check in all 4 directions left,right,top,bottom 
            self.dx=[0,1,0,-1]    #this is x coordinate directions 
            self.dy=[1,0,-1,0]    #this is y coordinate directions
            
            
        def isValidOceanCell(self,row,col,heights,height,vis):  #this method is used to verify if the cells have already been visited or if the cell can be visited or not
            if  vis[row][col]==-1:
                return False
            elif heights[row][col]<height:
                return False
            else:
                return True
            
        def isValid(self,row,col):  #this method is used to verify if the cells are valid or not means they are in range of 2D array matrix
            if row<0 or col<0 or row>=self.Row or col>=self.Col:
                return False
            else:
                return True
            
        def dfs(self,st,heights,vis):  #this method is used to do the dfs on each cell
                reachableCells=set()  #this set stores the cells that are valid
                while st:
                    prows,pcols=st.pop()
                    if self.isValid(prows,pcols):
                        if self.isValidOceanCell(prows,pcols,heights,heights[prows][pcols],vis):
                            reachableCells.add((prows,pcols))
                            vis[prows][pcols]=-1
                        for i in range(4):
                            adjx=prows+self.dx[i]
                            adjy=pcols+self.dy[i]
                            if self.isValid(adjx,adjy):
                                if self.isValidOceanCell(adjx,adjy,heights,heights[prows][pcols],vis):  #this is the main line here, before appening the cells in stack we are checking if these cells are visited before or if they have a height> their parent cell
                                            st.append([adjx,adjy])
                return reachableCells
            
            
        def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 
            self.Row=len(heights)
            self.Col=len(heights[0])
            self.pacific_vis = [[1 for _ in range(self.Col)] for _ in range(self.Row)]  #matrix used to store which cells are visited for pacific
            self.atlantic_vis = [[1 for _ in range(self.Col)] for _ in range(self.Row)]  #matrix used to store which cells are visited for atlantic
            pacificCells=set()   #used to store all the cells where water to pacific can go
            atlanticCells=set()  #used to store all the cells where water to atlantic can go
            
            #pacific loop for left edge cells :
            for row in range(self.Row):
                    st=[[row,0]] 
                    pacificCells|=self.dfs(st,heights,self.pacific_vis)  #| set union to store all the returned cells by dfs
            #pacific loop for top left edege cells
            for col in range(1,self.Col):
                st=[[0,col]]
                pacificCells|=self.dfs(st,heights,self.pacific_vis)
            #atlantic loop for right edge cells
            for row in range(self.Row):
                st=[[row,self.Col-1]]
                atlanticCells|=self.dfs(st,heights,self.atlantic_vis)
            #atlantic loop for bottom edge cells
            for col in range(self.Col-1):
                st=[[self.Row-1,col]]
                atlanticCells|=self.dfs(st,heights,self.atlantic_vis)
                
            commonCells=pacificCells&atlanticCells  #cell intersection to get the common cells from both the sets
            return list(commonCells) #return lists of cells

sol=Solution()
val=sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])    
print(val) 
                       
                            
#i was stuck as to how to compare the current cell to next cell to see if it has less height so that wateer can flow to its adjacent cells
#this was solved using a valid check right before putting the adjacent cells to stack , this way any adjacent cells that are to the base cells will get compared to its base cell height before appending to stack, it looks like bfs, but we are using stack so it is still DFS as it goes deep first
            
            
        
        