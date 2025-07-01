from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        sortedNums=sorted(count.items(),key=lambda x:x[1])
        return [key for key,value in sortedNums][-k:]
    
sol=Solution()
nums = [1,1,1,2,2,3], k = 2
val=sol.topKFrequent(nums,k)
print(val)

        