import heapq
from typing import List;

#this solution is very easy using priority queue

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[float('-inf')] * k
        for indx in range(len(nums)):
            heapq.heappush(self.heap,nums[indx])
            if len(self.heap)>k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        tempheap=self.heap
        heapq.heappush(tempheap,val)
        heapq.heappop(tempheap)
        return tempheap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)