
from typing import List

class Solution:
    
    #we are using kadane algorithm to find the maximum sum from subarrays of the nums array. Just a note that you can not use sliding window technique since the subarray size is dynamic and does not have a fixed size
    #kadane algo is simple that just add all the elements nums[i] in sum and if the sum gets negative start over by sum=0 and start a new sub array. just make sure to make totalsum=nums[0] because if all the elements in the array are negative than the best output is -1.
    def maxSubArray(self, nums: List[int]) -> int:
        sums=i=0
        totalSum=nums[0]
        while i<len(nums):
            sums=sums+nums[i]
            if sums>totalSum:
                totalSum=sums
            if sums<0:
                sums=0
            i=i+1
        return totalSum
            