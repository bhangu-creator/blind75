from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n=len(nums)
        indicesArray=[False]*n
        for i in range(n):
            if nums[i]==key:
                start=max(0,i-k)
                end=min(n-1,i+k)
                for j in range(start,end+1):
                    indicesArray[j]=True
        return [i for i in range(n) if indicesArray[i]]
#for every index j where nums[j] == key, all indices in the range j - k to j + k are k-distant indices

sol=Solution()
val=sol.findKDistantIndices([3,4,9,1,3,9,5],9,1)
print(val)

