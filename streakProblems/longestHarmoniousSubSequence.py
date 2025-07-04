from typing import List
from collections import Counter

class Solution:
    #intuation is just use counter to count the frequencies and then just search if two pairs of frequencies exist which is x and x+1 and then just group them together and return the max output
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