from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        indx=0
        returnInterval=[]
        while indx<len(intervals) and newInterval[0]>intervals[indx][1]:
            returnInterval.append(intervals[indx])
            indx+=1
        while indx<len(intervals) and intervals[indx][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],intervals[indx][0])
            newInterval[1]=max(newInterval[1],intervals[indx][1])
            indx+=1
        returnInterval.append(newInterval)
        while indx<len(intervals):
            returnInterval.append(intervals[indx])
            indx+=1
        return returnInterval
        
#the intuation is that the new interval can be placed at 3 possible position:
#it can come directly at front or it can come directly at last or it can come directly overlapped we have defined 3 while loops for each case