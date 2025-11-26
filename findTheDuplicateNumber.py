#O(n) time with O(1) space, we used slow and fast method of linked list as its a special case
#where length of list is n+1 and all the nums in list are in range (1,n)

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sindx,findx=nums[0],nums[nums[0]]
        while sindx!=findx:
            sindx=nums[sindx]
            findx=nums[nums[findx]]
        sindx=0
        while sindx!=findx:
            sindx=nums[sindx]
            findx=nums[findx]
        return sindx

