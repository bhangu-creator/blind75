from collections import deque
from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        res=[]
        n=len(nums)
        left=0
        for right in range(n):
            num=-nums[right]
            heapq.heappush(heap,(num,right))
            if (right-left)+1==k:
                while heap and heap[0][1]<left:
                    heapq.heappop(heap)
                if heap:
                    res.append(-heap[0][0])
                left+=1
        return res
#this solution has O(nlogn) time complexity and O(n) space , we use max heap to get the maximum available element from each window
#and then we use lazy deletion to pop the values that are no longer needed, main check is if indx<left means that indx is now out of current window and we can safely pop it from heap

#this can be done in O(n) time and space using monotonic queue , code is as follows

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=deque()
        res=[]
        n=len(nums)
        left=0
        for right in range(n):
            #storing only the indices which are present inside the current window
            while queue and queue[0]<right-k+1:
                queue.popleft()
            #maintaing the monotonic queue only with the decreasing order 
            while queue and nums[queue[-1]]<nums[right]:
                queue.pop()
            queue.append(right)
            #store the max value present inside the window
            if right>=k-1:
                res.append(nums[queue[0]])
        return res
            
            
#the time and space is O(n) 
#the intuation is that lets say a window is [1,3,5] now lets say a new element came which is 6 so now all other elements 1,3,5 are smaller than 6 that means
#now they have become useless meaning they can never be the max in any new or current window since 6 is present inside the window so we compare the values from back and one by one get rid of smallest elements 
#this can also help us make the queue monotonic decreasing order
#we also check if the top max element is outside the window if yes than we pop it
#and for all the valid windows we just simply store the max in res and return it 
            
            
            
            
