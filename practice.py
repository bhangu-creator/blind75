from collections import defaultdict
from collections import deque
from typing import List
import heapq

heap=heapq

class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        furthest_jump=nums[0]
        steps=0
        indx=0
        while furthest_jump<n-1:
            jump=furthest_jump
            steps+=1
            while indx<=jump:
                furthest_jump=max(furthest_jump,nums[indx]+indx)
                indx+=1
            if furthest_jump>=n-1:
                steps+=1
                return steps  
        steps+=1
        return steps


        

sol=Solution()

bol=sol.canJump([8,2,1,1,1,1,0,8,9])
print(bol)
        




