
from typing import List

class Solution:
    
    #this problem is very easy and can be solved using 2 pointers, there is only 2 points that we need to know to solve this problem
    #first point is what do we need? we need the Maximum Area that we can get for the container to hold the water
    #by common sense we can conclude that maximum area = maximum height * maximum width ( since it is a 2d it is gonna be rectangle)
    #So since there is a graph , you can imagine the two lines , 1 on left and 1 on the far right as the walls or sides of the container 
    # NOW IMPORTANT - there is mentioned that the container should not be slant or water should not spill, so In the beginning we will check which wall is larger , left or right, we will move the pointer of the wall which is smaller , we are doing this because of this logic since we want the maximum area , we can only get as if we have max area or max width but when we use 2 pointers we are moving inwards
    #which will make the width lower, so we need another attribute to be larger , that is gonna be height so we will greedely reserve our max height /wall and move towards small height/ wall, at each iteration where we move our pointers we will calculate our  area
    #in the end we will return the max area out of all the calculated area
    #[tip : imagine the diagram as a rectangular bowl in which water is present , so if you are decreasing the width you have to increase the height if you want the water to not spill]
    
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxArea=float('-inf')
        while left<right:
            area=min(height[left],height[right]) * (right-left)
            maxArea=max(area,maxArea)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxArea
sol = Solution()
res = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(res)
            
            


        
        
        