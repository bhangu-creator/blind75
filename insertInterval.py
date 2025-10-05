
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        resArr=[]
        indx=0
        while indx<len(intervals) and intervals[indx][1]<newInterval[0]:
            resArr.append(intervals[indx])
            indx+=1
        while indx<len(intervals) and newInterval[1]>=intervals[indx][0]:
            newInterval[0]=min(newInterval[0],intervals[indx][0])
            newInterval[1]=max(newInterval[1],intervals[indx][1])
            indx+=1
        resArr.append(newInterval)
        while indx<len(intervals):
            resArr.append(intervals[indx])
            indx+=1
        return resArr
#intuation is that we just need to put the new interval in the already interval list
#now to do that we can just use first loop to look where to put the new interval
#in second loop we can put the new interval while comparing the interval list for the overlapping intervals 
# then in third loop when the overlapping is donejust put the remaining intervals in the new list
# the time complexity is O(n) and space is O(1) if the return string is not counted

        