from typing import List

class Solution:


    #the intuation for this problem is very simple, we will first sort the intervals so that we can move in 1 direction then we will just compare each interval, if the interval is non overlapping then we will just increase our initial interval to the range of that non overlapping interval
    #but if the intervals are overlapping than there are two cases the end of that interval is outside of the first or the second interval is totaly inside the first interval. In any case we will simply increase the range of initial interval to the minimum of those two becasue that way we will potentially have less overlapping intervals in future
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minNumberToRemove=0
        intervalMain=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<intervalMain[1]:
                minNumberToRemove+=1
                intervalMain[1]=min(intervalMain[1],intervals[i][1])
            else:
                intervalMain[1]=intervals[i][1]
        return minNumberToRemove

sol=Solution()
val=sol.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])
print(val)