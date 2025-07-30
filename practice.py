from collections import defaultdict
from typing import List
import heapq


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def dfs(k,operations):
            if k==1:
                return 0
            half=1
            indx=0
            while half*2<k:
                half*=2
                indx+=1
            if operations[indx]==1:
                trans=dfs(k-half,operations)+1
            else:
                trans=dfs(k//2,operations)
            return trans
        trans=dfs(k,operations)
        return chr(97+(trans%26))



          
sol=Solution()
res=sol.kthCharacter(5,[1,0,0])
print(res)







