from collections import defaultdict
from collections import deque
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        maxFreeTime=0
        left=right=0
        free=0
        gap=0
        startTime.append(eventTime)
        endTime.append(eventTime)
        print(startTime)
        print(endTime)
        while right<len(startTime):    
            if (right-left)+1<=k+1:  
                gap=startTime[right]-gap
                free=free+gap
                maxFreeTime=max(maxFreeTime,free)
                gap=endTime[right]
                right+=1
            else:
                if left==0:
                    free=free-(startTime[left]-0)
                    left+=1
                else:
                    free=free-(startTime[left]-endTime[left-1])
                    left+=1
        return maxFreeTime
        


sol=Solution()
bol=sol.maxFreeTime(34,2,[0,17],[14,19])
print(bol)
        




