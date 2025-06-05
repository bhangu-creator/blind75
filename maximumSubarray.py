
from typing import List

class Solution:
    
    #we are using kadane algorithm to find the maximum sum from subarrays of the nums array. Just a note that you can not use sliding window technique since the subarray size is dynamic and does not have a fixed size
    #kadane algo is simple that just add all the elements nums[i] in sum and if the sum gets negative start over by sum=0 and start a new sub array
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        sumOfNumbers=0
        for index in range(0,len(nums)):
            sumOfNumbers=sumOfNumbers+nums[index]
            maxSum=max(maxSum,sumOfNumbers)
            if sumOfNumbers<0:
                sumOfNumbers=0
        return maxSum
            