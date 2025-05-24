from typing import List

class Solution:

    # code here
    # hash data structure is used to solve this problem. 
    #hash data structure is the best approach for this problem as it gives O(n) time complexity
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in sum_dict:
                return[i,sum_dict[complement]]
            else:
                sum_dict[nums[i]]=i
                

arr=[3,2,4]
sol = Solution()
res=sol.twoSum(arr,6)
print(res)