from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0
        for num in freq:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])
        return max_len


sol=Solution()
nums=[1,3,2,2,5,2,3,7]
val=sol.findLHS(nums)
print(val)