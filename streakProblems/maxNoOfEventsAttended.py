import heapq
from typing import List


class Solution:

    #intuation is like viewing a calander we will view all the portion where events are planned from first day to last day
    #at every day we will see how many events we need to attend, we will maintain their last day in heapq and we will just pop 1 event after each day to ensure that we have attended an event with minimun endday which can give us more window to attend events with max ennddy
    #at every day we will aslo get rid of expired events if their endday is now less than current day, we will do this by simply poping the heap
    #at evey pop after a day it means we have attended the event that day and we will count the no of pop operations and will return it at end
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        lastday=max(end for start,end in events)
        heap=[]
        firstday=events[0][0]
        i=0
        attend=0
        for day in range(firstday,lastday+1):
            while heap and heap[0]<day:
                heapq.heappop(heap)
            while i<len(events) and events[i][0]==day: 
                heapq.heappush(heap,events[i][1])
                i+=1
            if len(heap)>0:
                heapq.heappop(heap)
                attend+=1  
        return attend



            


        