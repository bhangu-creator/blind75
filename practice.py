from typing import List
from collections import deque
# Definition for a binary tree node.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        minNumberToRemove=0
        intervalMain=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<intervalMain[1]:
                minNumberToRemove+=1
            else:
                intervalMain[1]=intervals[i][1]
        return minNumberToRemove

        
    
sol=Solution()
val=sol.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])
print(val)
        
        