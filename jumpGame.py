from typing import List

class Solution:
    
    
    #we solved this problem with the help of greedy Approach. At every index/step we are calculating the furthest index that we could go while standing at that current index and then storing that furthest , if at next steps we found a greater further distance than the stored one we will update our furthest.
    #but if get to an index which is greater than the furthest index we could go that would indicate us that we have gone out of the furthest range that we could have gone. Then we return False.
    #if furtherIndex at any step got>= len(nums)-1 we will return True
    #if the loop ended for input=0 than we simply return True
    def canJump(self, nums: List[int]) -> bool:
        furthestJump=0
        for i in range(0,len(nums)):
            if furthestJump>=len(nums)-1:
                return True
            if i>furthestJump:
                return False
            furthestJump=max(furthestJump,(nums[i]+i))
 


        
sol=Solution()
val=sol.canJump([3,2,1,0,4])
print(val)