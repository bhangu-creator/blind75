from typing import List

#this is just intuative way where as you know at each height the max water that can be trapped is 
#going to be the min height from left,right - the actual height but there is also 1 trick of getting the max left and max right height also 
#time and space is O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lmax,rmax=[0] * n,[0] * n
        maxleft=height[0]
        maxright=height[n-1]
        right=n-1
        maxArea=0
        for indx  in range(n):
            maxleft=max(maxleft,height[indx])
            lmax[indx]=maxleft
            maxright=max(maxright,height[right])
            rmax[right]=maxright
            right-=1
        for indx in range(n):
            maxArea+=min(lmax[indx],rmax[indx])-height[indx]
        return maxArea


#the same problem can be solved in O(1) space by using two pointers and a new intuation. the intuation is that whichever side from left and right is min we will move from that side
#why because lets say that height at left<right now no matter how many water is trapped between these heights the water will always depend upon the min height so if min height is at left 
#then we will simply check what is the max left means how far above water can go at current height and then use the formula to compure the water trapped

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxleft,maxright=0,0
        left,right=0,n-1
        totalwater=0
        while left<right:
            maxleft=max(maxleft,height[left])
            maxright=max(maxright,height[right])
            if height[left]<height[right]:
                totalwater+=min(maxleft,maxright)-height[left]
                left+=1
            else:
                totalwater+=min(maxleft,maxright)-height[right]
                right-=1
        return totalwater
            










