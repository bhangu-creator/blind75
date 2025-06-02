from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        furtherIndex=nums[0]
        maxJump=0
        count=0
        for i in range(0,len(nums)):
            if furtherIndex>=len(nums)-1:
                count=count+1
                return count
            maxJump=max(maxJump,(i+nums[i]))
            if i==furtherIndex:
                furtherIndex=maxJump
                count=count+1
        return count

        
sol=Solution()
val=sol.jump(nums = [1, 1, 1, 1])
print(val)