from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkK(k):
            noOfHrs=0
            for indx in range(len(piles)):
                noOfHrs += math.ceil(piles[indx] / k)
                if noOfHrs>h:
                    return False
            return True
            
        left,right=math.ceil(sum(piles) / h),max(piles)
        k=0
        while left<=right:
            mid=(left+right)//2
            if checkK(mid):
                k=mid
                right=mid-1
            else:
                left=mid+1
        return k

#ok so the problem is pretty self explanotary so just followed the story to the code and used binary search for optimization
#time is O(n)logm where n is length of piles arraya and m is the max pile value in array with O(1) space
