from collections import defaultdict
from collections import Counter
import random
from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=defaultdict(int)
        for num in nums:
            freq_map[num]+=1
        listofpairs=[(num,freq) for num,freq in freq_map.items()]
        def partition(left,right,pivotIndex):
            pivot=listofpairs[pivotIndex][1]
            listofpairs[pivotIndex],listofpairs[right]=listofpairs[right],listofpairs[pivotIndex]
            startIndex=left-1
            for rightIndex in range(left,right):
                if listofpairs[rightIndex][1]<pivot:
                    startIndex+=1
                    listofpairs[rightIndex],listofpairs[startIndex]=listofpairs[startIndex],listofpairs[rightIndex]   
            listofpairs[startIndex+1],listofpairs[right]=listofpairs[right],listofpairs[startIndex+1]
            return startIndex+1
        def quickselect(left,right,kth):
            if left==right:
                return
            pivotIndex=random.randint(left,right)
            pivotIndex=partition(left,right,pivotIndex)
            if k==pivotIndex:
                return
            if k<pivotIndex:
                quickselect(left,pivotIndex-1,kth)
            else:
                quickselect(pivotIndex+1,right,kth)
        n=len(listofpairs)            
        quickselect(0,n-1,n-k)
        return [num for num,freq in listofpairs[n-k:]]



            

        