
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        mergeinterval=intervals[0]
        for indx in range(1,len(intervals)):
            if intervals[indx].start<mergeinterval.end:
                return False
            mergeinterval=intervals[indx]
        return True
#intuation is simple if any overlapp intervals are found the meetings can not be attended m if not then the can 
#time complexity is O(nlogn) and space is O(1)