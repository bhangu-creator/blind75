

#problem is about duplicacy so using a set is preferred
#loop through the array and if element exists in the set return true and if not return flase

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set= set()
        for x in nums:
            if x in nums_set:
                return True
            else:
                nums_set.add(x)
        return False
    
bol = Solution()
res = bol.containsDuplicate([3,3])
print(res)