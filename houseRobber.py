
#this is the top down approach where the result is at dp[0] ,we start from first problem like how 
#much money can be robbed at indx 0 and then we go towards n-1. O(n) time and space

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1] * len(nums)
        def takeorleave(indx):
            if indx>=len(nums):
                return 0
            if dp[indx]>=0:
                return dp[indx]
            take=nums[indx]+takeorleave(indx+2)
            skip=takeorleave(indx+1)
            dp[indx]=max(take,skip)
            return dp[indx]
        return takeorleave(0)

#here is the bottom up approach with O(n) space , it may feel like a top down but only beacuse we go to each indx
#and we compute the best result for that indx 
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0] * (n+2)
        for indx in range(n-1,-1,-1):
            take=nums[indx]+dp[indx+2]
            skip=dp[indx+1]
            dp[indx]=max(take,skip)
        return dp[0]
            
        
#here is the bottom up approach for O(1) space, since at each indx we only need two things indx+1 and indx+2 so we can
#just store the values and use them further
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        next1,next2=0,0
        for indx in range(n-1,-1,-1):
            curr=max(nums[indx]+next2,next1)
            next2=next1
            next1=curr
        return curr
        
            
        

            
        