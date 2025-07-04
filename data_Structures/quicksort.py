class Solution:

    #the idea is to just get a pivot element and then compare the rest of elements with that , and just group the elements smaller than pivot to left side and bigger to right side
    #do this recursively and in end you will have a sorted array
    #time complexity is O(nlogn) and space O(logn)
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
    
    #this is the pure recursive approach to return the sorted array instead of doing the sorting inplace
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