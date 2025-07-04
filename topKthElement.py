from typing import List
import heapq,random

class Solution:

   #this is very simple heapq solution , it is made more optimized by just maintaining only k length heap so that the kth element will poped out first after the loop
   #time Onlogk  where k is the size of heap and n is tota no of elements in nums as total n numbers are pushed in heap and the size of heap is k so due to binary tree structre this is the time complexity and space is O(k) 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

        
     #this is hybrid bucket plus counting solution. basically we found the range of numbers which can be present inside the nums array after doing that we created buckets for that many numbers
     # then as the array can contain the negative numbers so we start the index from minvalue by subtracting evrry value from minvalue that way all the numbers will have valid indices. so after using the loop we calculate the frequencies of all the numbers in array
     # after that we start a loop on range of max value to min value and for each value we see if the bucket is empty or not if it is not than we subtract the k with no of freq in that bucket. when k<=0 we know we got our number
     # the idea is we are looking from max number to min so  in that way we are going in sorted way and along the way we are also subtracting the frequencies so that way we are just traversing a sorted array without sorting the array
     # Time complexity is O(n) and time complexity is O(n)   
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)
        buckets=[0]*(max_value-min_value+1)
        for num in nums:
            index=num-min_value
            buckets[index]+=1
        for num in range(max_value,min_value-1,-1):
            if buckets[num-min_value]!=0:
                k-=buckets[num-min_value]
                if k<=0:
                    return num
                
    #here we are using the quickselect but we are using a new 3way version basically we are selecting the pivot randomly then we are creating 3 lists left with numbers greater than pivot , middle numbers same as pivot and right numbers smaller than pivot
    #then we just check if the size of left list is greater than k that would mean that our kth element is in that list so we recursively call left side for k 
    #if not than we check if the size of left list + size of middle list is greater than or equal to k if this is true than surely our k lies in middle and since all the middle elements are same as pivot we simply returns the value of the pivot
    #if not then we simply call the recursion for right side and we subtract k with len of left and middle because since we are looking into right list then that would means the first k elements which are present in left and middle are not valid so we subtract the length to make sure that our new k represents correct value which is how much far is k from left to right
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot=random.choice(nums)
        left= [val for val in nums if val>pivot]
        middle=[val for val in nums if val==pivot]
        right=[val for val in nums if val<pivot]
        if len(left)>=k:
            return self.findKthLargest(left,k)
        elif len(left)+len(middle)>=k:
            return pivot
        else:
            return self.findKthLargest(right,k-len(left)-len(middle))
        

