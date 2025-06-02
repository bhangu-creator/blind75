from typing import List

class Solution:
    
    #the intiuation for this problem is first start a loop over the whole array from index 1 and starts comparing the nums[1] and nums[1-1] index till the end of the loop
    #compare the two elements to see if they are same or not , if they are both same then do nothing but if they are not same means they are not duplicate so you should place the non duplicate element in the place of the duplicate element whose index will be stored in idx variable
    #after placing the non duplicate element at place of duplicate element increment the index of duplicate variable idx
    #there is a observation if follow the above approach our code is only placing the non duplicate element at place of duplicate only when we know both elements are not same
    #there may be two edge cases in the loop, first is if the last two elements of array are not same that our code will not place the last non duplicate element at place of duplicate element since there is nothing to compare to the last element as the loop will get finished.
    #the another edege case is if the last two elements of array are same than we again won't meet the element not same condition and therefore we won't be able to put that element at place of  duplicate index idx
    #so to handle these Test cases we simply assigned the last index of array to idx of duplicate elements when loop is finished since from our observation from the last two cases both the elements deserves to be at duplicate idx and then we increment it
    
    def removeDuplicates(self, nums: List[int]) -> int:
        idx=0      #initialzing the duplicate index
        for i in range(1,len(nums)):   #start the loop  from index 1 to compare two elements of array
            if nums[i-1]!=nums[i]:    #if two elements of the loop are not equal than that means we can put the first non equal element on duplicate idx and then increment the idx
                nums[idx]=nums[i-1]
                idx+=1
                
          #if the two elements in the array are same than we will not do anything and will not change the idx value, we will only change the idx value when we get two non equal values and needs to indert 1 to the idx      
                
        nums[idx]=nums[len(nums)-1]   #as i explained above our code logic leaves the last element without check so need to place that manually in the idx and then increment it
        idx=idx+1
        print(nums)
        return idx


sol=Solution()
val=sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(val)
