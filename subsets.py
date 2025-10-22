from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        myset=[]
        def backtrack(subset,indx):
            myset.append(subset.copy())
            for i in range(indx,n):
                subset.append(nums[i])
                backtrack(subset,i+1)
                subset.pop()
        backtrack([],0)
        return myset
    #ok so it is purely backtracking problem, to undertstand the problem please draw a recursion tree starting from [].
    #time is On*2^n since a 2^n subsets cab be derived from an array space is avg O(n) if result array excluded
