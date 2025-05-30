#first we will apply a method which can be O(n) but I am only able to make it work to get (On2)
#i got this idea from a hint , where it is said that if in three numbers x+y+z=0 if we know one number lets say x than essentially this problem just becomes 2sum problem so... I will implemet 2 sum solution on each element of nums and will make it efficent after

#this is the brute force way, it is very very inefficent

from typing import List

class Solution:
    def threeSumBrute(self, nums: List[int]) -> List[List[int]]:
        retArr={}
        for j in range(0,len(nums)):
            x=nums[j]  #fixed number out of 3
            recDict=set()
            for i in range(0,len(nums)):
                if i==j:
                    continue
                if -x-nums[i] in recDict:
                    retArr.add(tuple(sorted(([x,nums[i],0-(x)-nums[i]]))))
                else:
                    recDict.add(nums[i])
        return  [list(t) for t in retArr]
    
    
    
    #to make this code more efficent , i got the hint from leetcode to first sort the array and then apply two pointer algo, let's try that shall we?
    #ok so now listen on how did we solved this problem ,first thing is sort the array. why does sorting important because than we can apply two pointers algo whose time complexity is o(n).
    #after array is sorted we will make the first element of array as fixed element in 1 of the triples. so to find the rest two elements we will start the loop from the second element
    #first pointer will start from the next index of which is our fixed element and right pointer will start from the last element of the array.In this way we can apply the two pointer in front of the fixed element to find the two missing elements just like two sum problem
    #we will do this process for each element of the array
    #To deal with duplicacy, the first duplicacy will come when looking for fixed elements.we will check if the fixed element is not at 0 position and if current fixed element is equal to previous one than we can skip this elemt and go to next one because since it is sorted array we have already found the appropriate triplet for the current element .
    #when we will found the valid triplets inside the loop we will increase the i pointer and decrease the j pointer since both the elements at pointer are now stored. So we will check at that point if the elements at new pointer are same as previous if they are than we can skip these elements since we have already calculated the valid triplet for them
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retArr=[]
        nums.sort()
        for first in range(0,len(nums)):
            x=nums[first]  #fixed number out of 3
            if first>0 and nums[first]==nums[first-1]:
                continue
            i=first+1;j=len(nums)-1
            while i<j:
                if x+nums[i]+nums[j]>0:
                    j=j-1
                elif x+nums[i]+nums[j]<0:
                    i=i+1
                else :
                    retArr.append([x,nums[i],nums[j]])
                    i=i+1
                    j=j-1
                    while i<j and nums[i]==nums[i-1]:
                        i=i+1
                    while i<j and nums[j]==nums[j+1]:
                        j=j-1
        return  retArr
                
                    
                
        
                    
                    
sol=Solution()
val=sol.threeSum([-1,0,1,2,-1,-4])
print(val)
                


                    
                
        