from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uniq_elem=set()
        uniq=0
        uniq_max=0
        left=0
        for right in range(len(nums)):
            if nums[right] not in uniq_elem:
                uniq_elem.add(nums[right])
                uniq+=nums[right]
                uniq_max=max(uniq_max,uniq)
            else:
                while nums[right] in uniq_elem:
                    uniq-=nums[left]
                    uniq_elem.remove(nums[left])
                    left+=1
                uniq_elem.add(nums[right])
                uniq+=nums[right]
        return uniq_max
    #this is a cumilative sum approach basically wwe are reducing the amount of element deletion and moving left 1 by 1 to direct jumps
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cus=[]
        sums=0
        uniq_elem={}
        for num in nums:
            sums=sums+num
            cus.append(sums)
        left=right=maxSum=elemSum=0
        while right<len(nums):
            if nums[right] in uniq_elem and uniq_elem[nums[right]] >= left:
                left=uniq_elem[nums[right]]+1
            uniq_elem[nums[right]]=right
            if left>0:
                elemSum=cus[right]-cus[left-1]
            else:
                elemSum=cus[right]
            maxSum=max(maxSum,elemSum)
            right+=1
        return maxSum
 


        