class Solution :
    def insertionSort(self,nums):
        for i in range(1,len(nums)):
            j=i-1
            key=nums[i]
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
            
        return nums
    
sol=Solution()
nums=[3,4,0,2,1]
val=sol.insertionSort(nums)
print(val)
