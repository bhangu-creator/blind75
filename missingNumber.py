#There are 3 approcahes to solve this problem :
#Subtraction Method - which we used , basically we know all the elements in the array are from 0-n so we first get the sum of the n numbers, now we also know all the numbers inside the array so we get the sum of those numbers and then just subtract the n-(insideNumsNumber) , and we get the missing number
#XOR method- XOR have a associative and commutative property. Logic is simple if you observe than you can notice that each indices of array should be present as an element inside the array so if we XOR each indices with each element inside then we can get the remaining number. basically saying missing no = missing no ^ i ^ nums[i].
#Sort the array first then apply binary search to search the element. This solution will have O(logn) time complexity. In Binary search if the nums[mid] == mid and if nums[mid]>mid meaning in both cases the missing number should be on their left side.also maybe this mid can also be the missing number so store it in var.If nums[mid]<mid than the missing elemet might on right side

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        total=n*(n+1)//2
        return total-s
            
            
sol = Solution()
val = sol.missingNumber([3,0,1])
print(val)