from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def dfs(k,operation_index):
            if k==1:
                return 0
            half=1
            depth=0
            while half*2<k:
                half*=2
                depth+=1
            newIndex=max(0,operation_index-depth)
            if operations[depth]==0:
                return dfs(k-half,newIndex)
            else:
                return dfs(k-half,newIndex)+1
        return chr(ord('a')+dfs(k,len(operations)-1)%26)