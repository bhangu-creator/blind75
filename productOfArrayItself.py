from typing import List
import math

class Solution:
                
    #this problem can be solved by knowing that the value at i is going to be product of all elements that comes before i meaning product of all prefixes * all the elements that comes after i meaning product of all the suffix elements
    #this problem has some restriction, we have to only use solution with O(n) complexity and also we are not allowed to use divisible(/) character, these restrictons make this problem hard
    #but after knowing the first point we can focus on getting the product of prefix and suffix and can store them output array as the output array is not getting computed in space complexity so space complexity can be O(1)
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=postfix=1
        retArray=[1]*len(nums)
        for i in range(1,len(nums)):
            prefix=prefix*nums[i-1]
            retArray[i]=prefix
        for i in range(len(nums)-2,-1,-1):
            postfix=postfix*nums[i+1]
            retArray[i]=retArray[i]*postfix
        return retArray
            
            
sol=Solution()
val=sol.productExceptSelf([1,2,3,4])
print(val)
            
