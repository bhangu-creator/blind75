class Solution :

    #insertion sort is basically saying fixing nums[0] as sorted and then comparing each element after that with the sorted elements at left side and just keep on shifting them if the compared element is smaller then them and when a index is found where the element is not smaller just place that key element there
    #time complexity is O(n)square and space complexity is O(1)
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
