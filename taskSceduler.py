import heapq;
from collections import deque,Counter;
from typing import List;


#time complexity of this solution is avg O(n). The main intuation is to always use the characters with the highest frequencies.
#we use maxheap to keep track of the highest freq character at each time. and we use a time queue which keeps track of the cooldown of each character.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        freq=Counter(tasks)
        heap=[]
        cooldown=deque()

        for char,frq in freq.items():
            heapq.heappush(heap,(-frq,char))

        while heap or cooldown:
            time+=1
            if cooldown and cooldown[0][0]==time:
                cooltime,ngfrq,char=cooldown.popleft()
                heapq.heappush(heap,(-ngfrq,char))
            
            if heap:
                ngfrq,char=heapq.heappop(heap)
                frq= -ngfrq-1

                if frq>0:
                    cooldown.append((time+n+1,frq,char))
        return time


            


                


            



                
            