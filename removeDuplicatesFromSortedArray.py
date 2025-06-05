from typing import List

class Solution:
    
    #the intiuation for this problem is first start a loop over the whole array from index 1 and starts comparing the nums[1] and nums[1-1] index till the end of the loop
    #compare the two elements to see if they are same or not , if they are both same then do nothing but if they are not same means they are not duplicate so you should place the non duplicate element in the place of the duplicate element whose index will be stored in idx variable
    #after placing the non duplicate element at place of duplicate element increment the index of duplicate variable idx
    
    def removeDuplicates(self, nums: List[int]) -> int:
        idx=1     #initialzing the duplicate index
        for i in range(1,len(nums)):   #start the loop  from index 1 to compare two elements of array
            if nums[i-1]!=nums[i]:    #if two elements of the loop are not equal than that means we can put the first non equal element on duplicate idx and then increment the idx
                nums[idx]=nums[i]
                idx+=1
        return idx


sol=Solution()
val=sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(val)
