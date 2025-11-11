from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        posdict={}
        for indx in range(n):
            posdict[position[indx]]=indx
        position.sort()
        newSpeed=[0] * n
        time=[0]*n
        stack=[]
        noOfFleets=0
        for indx in range(n):
            val=position[indx]
            actIndx=posdict[val]
            newSpeed[indx]=speed[actIndx]
        for indx in range(n):
            time[indx]=(target-position[indx])/newSpeed[indx]
        for indx in range(n-1,-1,-1):
            if not stack or stack[-1]<time[indx]:
                stack.append(time[indx])
                noOfFleets+=1
        return noOfFleets
                    
#ok so the intuation behind this problem is that from target we will go to 0 distance and while doing
#this we will keep comparing if we can get a faster car if yes then that car will join fleet and the next 
#comparisons will be with the slowest out of those two

#time is O(nlogn) and space is O(n)