

from typing import List;
import heapq;

#very easy solution using minheap
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        if len (stones)==1:
            return stones[0]
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while heap:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone2!=stone1:
                heapq.heappush(heap,-(stone1-stone2))
            if len(heap)==1:
                return -heap[0]
        return 0