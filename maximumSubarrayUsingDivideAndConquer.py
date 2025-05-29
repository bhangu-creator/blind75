
from typing import List


#honestly even I don't know what I did here. when I get it I will update the code , until then ..
class Solution:
    
    def crossingArray(self,arr,left,mid,right)->int:
        sum=0
        leftSum=arr[mid]
        rightSum=arr[mid+1]
        for i in range(mid,left-1,-1):
            sum=sum+arr[i]
            if sum>leftSum:
                leftSum=sum
        sum=0
        for i in range(mid+1,right+1):
            sum=sum+arr[i]
            if sum>rightSum:
                rightSum=sum
        return leftSum+rightSum            
            
    def divideArray(self,arr,left,right)->int:
        if left==right:
            return arr[left]
        mid=(left+right)//2
        leftSum=self.divideArray(arr,left,mid)
        rightSum=self.divideArray(arr,mid+1,right)
        crossSum=self.crossingArray(arr,left,mid,right)
        totalSum=max(leftSum,rightSum,crossSum)
        return totalSum
    
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=self.divideArray(nums,0,len(nums)-1)
        return maxSum

sol=Solution()
val=sol.maxSubArray( [-2,1,-3,4,-1,2,1,-5,4])
print(val)
        
        
            