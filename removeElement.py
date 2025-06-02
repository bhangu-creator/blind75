from typing import List

class Solution:
    
    #The intiuation for this problem is we will do a loop over the array and at each index we will check if the value at the index is same as value or not
    #now if the value is same as the value on that index then we will store that index in variable like idx, we are doing this because since the index value is same as val we can put another value of the array at that inde which is not same as val
    #Now if the next value is not same as val that would mean that we should put this value to the stored idx value and we will aslo increment the idx since the previous idx is now occupied
    #so this way we will keep on looping the whole array storing the idx value in pointer where we can place the non val elements
    def removeElement(self, nums: List[int], val: int) -> int:
        idx=0  #intialize index pointer where we can place the non equal values as 0 
        for x in range(0,len(nums)): #loop through the whole array
            if nums[x]!=val:          #if the value is not equal to val means we can store this value to the idx pointer value which represent the index value where the equal val element is present
                nums[idx]=nums[x]
                idx=idx+1    #after placing the non equal val at idx we can increment the idx
        return idx        #return value of idx pointer which represents the idx till which we have placed the non equal values
    
sol=Solution()
sol.removeElement([3,2,2,3],3)