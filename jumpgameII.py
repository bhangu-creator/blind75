from typing import List

class Solution:
    
    
    #the intuation to solve this problem is that you want to get the minimum no of jumps to reach the end , so you should look for the maximum jump you can make at each index, the catch is that you can not just jump whenever you get a max jump that is bigger than the before index you were on , You need TO jump only on the MAXIMUM JUMP INDEX within the range of your first max JUMP. 
    #when you jump on the maximum jump you can jump on in the given range of the previous max jump you are on than you can increase the count and see if now you can reach the end or not, and keep on doing the same till end, and only jump when i==furtherindex or i>furtherindex(in my new leetcode sol), 
    #edge case is if there is only 1 element in the array than you are already at last place so just return 0 as min jump is 0
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        furtherIndex=nums[0]
        maxJump=0
        count=0
        for i in range(0,len(nums)):
            if furtherIndex>=len(nums)-1:
                count=count+1
                return count
            maxJump=max(maxJump,(i+nums[i]))
            if i==furtherIndex:
                furtherIndex=maxJump
                count=count+1
        return count

        
sol=Solution()
val=sol.jump(nums = [7,0,2,1,2,3,1,1,2,0,1,2,9,0,3])
print(val)