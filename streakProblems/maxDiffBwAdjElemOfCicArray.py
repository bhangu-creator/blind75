from typing import List

class Solution:
    
    #circular array is the array where the last element of the array and the first one are adjacent
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDiff=float('-inf')
        if len(nums)>2:
            maxDiff=max(maxDiff,abs(nums[0]-nums[len(nums)-1]))
        for i in range(1,len(nums)):
            maxDiff=max(maxDiff,abs(nums[i]-nums[i-1]))
        return maxDiff
    
    
sol=Solution()
val=sol.maxAdjacentDistance([1,4,9])
print(val)

        