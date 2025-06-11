from typing import List


class Solution:

    def findPivot(self,nums):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if mid<right:
                right=mid
            else:
                left=mid+1
        return nums[left]

    def findMin(self, nums: List[int]) -> int:
         pivot=self.findPivot(nums)
         return pivot




    
sol=Solution()
val=sol.findMin([3,4,5,1,2])
print(val)












