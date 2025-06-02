
from typing import List

class Solution:
    
    #There was a restriction on this problem to only solve it using O(logn) time complexity
    # This problem is needed to be solved using Binary Search since Binary search has O(logn) time complexity
    # A rotated array is a array which was sorted at first and then it was rotated by some k frequency. Rotated basically means shifting the last element to first for k times
    # This makes the rotated array kind of a merged array of two sorted arrays
    #The first thing we need to do to solve this problem is to find the pivot point of the rotated array, pivot point can be identifed as the index of the largest element in array or the index of smallest element in array, for this problem we are going as the small option
    #First issue was we need to find the pivot using modified Binary search, so we did that.The intiuation is when we get a mid of array then if the nums[mid] is greater than the right meaning we are at left side of the pivot so we can move towards right and vice versa if nums[mid] < right
    #after finding the pivot we can search the target in either in left array or right array depending upon in which array range does the target lies in 
    
    
    def searchElement(self, left, right, nums, target): 
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def findPivot(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left 

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1  
        if len(nums) == 1:
            return 0 if nums[0] == target else -1  
        if nums[0] <= nums[-1]:  
            return self.searchElement(0, len(nums) - 1, nums, target)

        pivot = self.findPivot(nums)
        
        if nums[pivot] == target:
            return pivot

        if target >= nums[0] and target <= nums[pivot - 1]:
            return self.searchElement(0, pivot - 1, nums, target)
        else:
            return self.searchElement(pivot, len(nums) - 1, nums, target)

    
sol=Solution()
val=sol.search([4,5,1,2,3],1)
print(val)
