
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        room=1
        heap=[]
        for interval in intervals:
            if heap and heap[0]>interval.start:
                room+=1
            elif heap and heap[0]<=interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap,interval.end)
        return room
#the intution is simplewe for each meeting we will only assign a new room if the ending time for any of the specific room is not ove yet
#if any of the rooms assigned the end time of party is over then we will just assig the new party end time to that room using minheap to store all the end time of meetings
#time complexity is Onlogn due to sorting and space is O(1)
            
            

