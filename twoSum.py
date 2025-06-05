from typing import List

class Solution:

    # code here
    # hash data structure is used to solve this problem. 
    #hash data structure is the best approach for this problem as it gives O(n) time complexity
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict={}
        
        #approach behind this problem is that x+y=target , so to get either x or y it will be x=target-y
        #so we will check for each element in the array that does target-y exists in the dict , if not that we will add y as key in dict with index as its value since we can get x as target-y if we search the rest of the array
        #then while looping we will get x which is target-y and as we have already stored (target-y) as x in the dict we will retrieve its index from that and return both the index as list
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