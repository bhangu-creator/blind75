from typing import List



class Solution:
    
    #watched a yt video to solve this problem via observation. The concept was simple. if all the values in the array are positive than max product will be product of all the values of array. If the no of -ve values in array are even then it is the same case since -ve and -ve cancel each other out. 
    #BUT if the -ve values in array are odd than that would mean that max product will be the one not containg one of those -ve value.
    #so if you can imagine you can say the max product can be on left side of a -ve value or on the right side of -ve value. So for each -ve number we can get the max prod of prefix and suffix for that -ve number. And after comparing the two we can get the max product of whole array
    #if when calculating product of prefix or suffix the product gets to 0 means we can just reset the prefix and suffix. Since max prod is stored we can keep on comparing them with it
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=suffix=1
        totalmax=float('-inf')
        for i in range(0,n):
            prefix=prefix*nums[i]
            suffix=suffix*nums[n-1-i]
            totalmax=max(totalmax,prefix,suffix)
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
        return totalmax
        

sol=Solution()
val=sol.maxProduct([3,-1,4])
print(val)



        

        