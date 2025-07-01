class Solution:
    def partition(self,arr,low,high):
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
    def quicksort(self,arr,low,high):
        if low<high:
            pi=self.partition(arr,low,high)
            self.quicksort(arr,low,pi-1)
            self.quicksort(arr,pi+1,high)
    
    def quicksortrecursion(self,nums):
        if len(nums)<=1:
            return nums
        pivot=nums[len(nums)//2]
        left=[val for val in nums if val<pivot]
        middle=[val for val in nums if val==pivot]
        right=[val for val in nums if val>pivot]
        return self.quicksortrecursion(left)+ middle + self.quicksortrecursion(right)

sol=Solution()
nums=[5,4,3,2,1]
val=sol.quicksortrecursion(nums)
print(val)    