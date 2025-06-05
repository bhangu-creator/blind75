from typing import List

class Solution:
    
    #this problem is similar to the problem where we are asked to remove all duplicates from the array whereas in this problem we are asked only to remove duplicates more than 2
    #so this means there should not be a same element in the array 3rd time in a row. If we find an element the 3rd time after repeating two times we will shift the right elements to the left
    #imagine you are building a new array inplace of the same array and you starts from the left side and then keep on adding elements ,and if you encounter the 3rd same element after 2 elements you override it, that is what we are doing here
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        idx=2   #we are intializing the index as 2 as we donot care about first two elements of new array our only focus is the 3rd element
        for i in range(2,len(nums)): 
            if nums[idx-2]!=nums[i]:  #will check if the 3rd element is equal to 1st , if it is not that would mean that it is at its right place and we can move forward and the new index to override will become idx+=1
                nums[idx]=nums[i]
                idx+=1
                #when the idx-2 element will be equal to i that would means that there are more than two same element present in range(idx-1,i) so we will keep the idx to modify as idx=i and when we found a new different element we place it at idx
                #to remember the intiuation more clearly imagine you are placing balls in a cardboard box , there are 2 balls already present of same/different colors and now when you want to place a new ball you can check the color of first ball that does it matches the ball you are about to be place in box or not which is 3rd ball, now you must think why not check 2nd also because the array /ball are in sorted order so if the 3rd ball matches 1st ball that surely will mean that 2nd ball is also same
        return idx