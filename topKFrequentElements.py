from collections import defaultdict
from collections import Counter
import random
from typing import List
import heapq

class Solution:


    #just basic approach, Onlogn
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        sortedNums=sorted(count.items(),key=lambda x:x[1])
        return [key for key,value in sortedNums][-k:]
    

    #this is the bucket sort method. basically create n buckets since the maxfreq can be n (all elements are same)
    #then just put the values in buckets in acoording to frequencies that way the top freq will be in last of buckets
    #do a loop over buckest from back if the freq exists  apend the nums in array and return it when reaches length ==k
    #time complexity is O(n) and space is alsp  O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=defaultdict(int)
        for num in nums:
            freq_map[num]+=1
        n=len(nums)
        buckets=[[] for _ in range(n+1)]
        for num,freq in freq_map.items():
            buckets[freq].append(num)
        retArr=[]
        for freq in range(n,0,-1):
            for num in buckets[freq]:
                retArr.append(num)
            if len(retArr)==k:
                return retArr
    

    #this method is used for quickselect to partially sort the list in a way that top k elements are on right side of pivot
    #here after calculating the frequency we convert it to list of tuple to get better access and iteration 
    #what we are essentially doing is that if you know quicksort you know that in that algo we sort the array from left using pivot in a way that all the smallest elements end up on its left side and we kind of build a subarray from left until we reach right end of main subarray
    #so given that here we are basically trying to build that sub array from left but only till n-k (n is length of list of pairs) this way all the elements from 0 to n-k will be smallest elements and from n-k to n-1 will be top k elements that we need
    #so when pivot reaches n-k basically meaning we have built a sorted sub array from left of this size it basically means that we have top k elements so we can return there values
    #timecomplexity average case - O(n) , worst case- O(n) square(picking bad pivot every time like last or first element), space complexity is O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map=defaultdict(int)
        for num in nums:
            freq_map[num]+=1
        listofpairs=[(num,freq) for num,freq in freq_map.items()]

        def partition(low,high,pivot):
            pivotFreq=listofpairs[pivot][1]
            listofpairs[pivot],listofpairs[high]=listofpairs[high],listofpairs[pivot]
            i=low-1
            for j in range(low,high):
                if listofpairs[j][1]<pivotFreq:
                    i+=1
                    listofpairs[j],listofpairs[i]=listofpairs[i],listofpairs[j]
            listofpairs[i+1],listofpairs[high]=listofpairs[high],listofpairs[i+1]
            return i+1
            
        def quickselect(left,right,kthsmall):
            if left==right:
                return
            pivotIndex=random.randint(left,right)
            pivotIndex=partition(left,right,pivotIndex)
            if kthsmall==pivotIndex:
                return 
            elif kthsmall<pivotIndex:
                quickselect(left,pivotIndex-1,kthsmall)
            else:
                quickselect(pivotIndex+1,right,kthsmall)
        n=len(listofpairs)
        quickselect(0,n-1,n-k)
        return [num for num,freq in listofpairs[n-k:]]
    




    #following is the method based on minheap or priority queue data structure, as we know priority queue in python works as a queue but inly diference is that the values pushed and popped out of this queue are in priority order 
    #basically it act as a Binary tree where each operation takes Ologn time to complete like insert or delete or pop
    #so intuation is if we just pushed the elements in heap queue in order of their priority of frequency and then just keep the length of queue as exactly k and keep poping out the smallest elements in the end we will be left with top k elements
    #time complexity is Onlogn as we do heap push or pull operation exactly n times
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap=[]
        freq_map=defaultdict(int)
        for num in nums:
            freq_map[num]+=1
        for num,freq in freq_map.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq,num in heap]
    
    
sol=Solution()
nums = [1,1,1,2,2,3], k = 2
val=sol.topKFrequent(nums,k)
print(val)

        