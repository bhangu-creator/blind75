from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        count,maxcount=0,0
        for num in nums:
            if num-1 not in nums:
                temp=num
                while temp in nums:
                    temp+=1
                    count+=1
                maxcount=max(maxcount,count)
                count=0
        return maxcount
#the intuation is just first use set to remove the duplicacy from nums, now for each num check if the num-1 exists in nums because if it does not exist
#that would mean that num is the mark where a new original sequence starts , when num is found then just keep on increasing num by +1 and keep checking if that exists in num
#after a sequence is ended use a maxcount variable to get the max sequence found
#the time complexity is O(n) because in the worst case all the nums is unique and the worst sequence is O(n) , space is O(1)
