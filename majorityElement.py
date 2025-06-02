from typing import List

class Solution:
    
    #the intiuation is very simple that the majority element will exist in array with its duplicate by its side for atleast once in the array and if not than it will exist at end of the array
    def majorityElement(self, nums: List[int]) -> int:
        maj=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==maj:
                count=count+1
            elif nums[i]!=maj:
                count=count-1
                if count<=0:
                    maj=nums[i]
                    count=1
        return maj
        

sol=Solution()
val=sol.majorityElement([2,1,2,3,2])
print(val)
        