from typing import List

class Solution:

    #this is a proper sliding window problem. The main observation to solving this problem is just that if we are given k operations to shift meeting that we have to understand that after shifting k meetings we will have k+1 gaps merged together
    #so the first approach is pretty simple just calculate all the gaps avilable and store them in the array and then use sliding window of size k+1 on that array to get the max output of k+1 merged gaps
    #Time and space complexity is O(n)
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps=[]
        freeTime=0
        for gap in range(len(startTime)):
            gaps.append(startTime[gap]-freeTime)
            freeTime=endTime[gap]
        gaps.append(eventTime-freeTime)
        maxFreeTime=0
        left=right=0
        free=0
        while right<len(gaps):
            if (right-left)+1<=k+1:
                free=free+gaps[right]
                maxFreeTime=max(maxFreeTime,free)
                right+=1
            else:
                free=free-gaps[left]
                left+=1
        return maxFreeTime

    #same intuation as above the only difference is instead of storing the gaps we are calculating them on the fly
    #space complexity is O(1) and Time complexity is O(n)
    #we are modifying the input array so .. thats not good , its good to handle last edge case outside of while loop but that a lot of unneccessary work so its good to make a copy of the array and do operation on that but that will be O(n) space so...
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        maxFreeTime=0
        left=right=0
        free=0
        gap=0
        startTime.append(eventTime)
        endTime.append(eventTime)
        while right<len(startTime):    
            if (right-left)+1<=k+1:  
                gap=startTime[right]-gap
                free=free+gap
                maxFreeTime=max(maxFreeTime,free)
                gap=endTime[right]
                right+=1
            else:
                if left==0:
                    free=free-(startTime[left]-0)
                    left+=1
                else:
                    free=free-(startTime[left]-endTime[left-1])
                    left+=1
        return maxFreeTime





 












 



