
from typing import List

class Solution:
    
    #ok so to solve this problem we have to first understand this, we have two Sorted arrays which we have to merge , but we have to merge one sorted array to another. In this case we have to merge nums2 into nums1 . we have given num1 length as m+n where m and n are no of elements in each array.
    #the first step is we need to understand we cannot sort this array when starting to loop from 0, we need to sort them from behind. Think of it as like they are two ascending order array, if we merge them both we will get single array of ascending order this means the last element of the merged array will be the largest element of that array
    #so if we compare the last elements of both array to see which is large we will get the largest element of the merged array, when we get the largest element of both array we will place it in the end of the first nums1 array. but if the element of nums2 is smaller than the last element of nums1 array than that would mean that last element of nums1 array is the largest of merged array so we will simply put the last valid element of nums1 to the last index of the nums1
    #and so on we will keep on comparing both the arrays untill we have all sorted nums2 elements in the nums1 array, but if some elements of nums2 still left than we can simply copy them in nums1 .
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:      #if nums2 is 0 i.e empty than there is nothing to merge to nums1 so return empty
            print(nums1)
            return 
        if m==0:   #if nums1 is 0 i.e empty than just copy all the elements of nums2 in nums1 and return empty
            nums1[:n] = nums2 
            print(nums1)
            return
        
        lastIndex=(m+n)-1  #lastindex is the last index (e.x 0) of nums1 where the sorted elements will be places
        
        while m>0 and n>0:    #loop will work untill either all nums2 elements will get sorted in nums1 or nums1 elements move to the right leaving space for nums2 elements
            
            if nums2[n-1]>=nums1[m-1]:    #if the last element of nums2 is greater than the last valid element of nums1
                nums1[lastIndex]=nums2[n-1] #then put the large element to last index of nums1 i.e in place of 0's
                lastIndex=lastIndex-1    #decrement the lastindex as it is now have been occupied
                n=n-1                    #decrement the index of nums2 as the previous element is now placed in num1 and is sorted
                
            else:                          #if the last element of nums1 is greater than nums2 then
                nums1[lastIndex]=nums1[m-1]   #swap the last valid large element of nums1 with lastIndex of nums1 this will free up the space for nums2 elements to be placed and get sorted      
                lastIndex=lastIndex-1      #same as before decrement the last index as the previous index is now been occupied
                m=m-1                      #decrement the index of nums1 as it is now moved to the end of nums1 and will get sorted after all elements of nums2 gets placed in nums1
                
                
        while n>0:                        #after the loop ends we will verify if n>0 this will tell us that if n is not 0 meaning that there are still some elements pending in nums2 which are not placed in nums1 and are not sorted
            nums1[lastIndex]=nums2[n-1]    #so we will start a loop untill n >0 and will start copying the nums2 elements from back to the lastIndex of nums1 , since we already created space in nums1 we can insert all the elements of num2 inside nums1 without issue
            n=n-1                         #keep on decrementing the indexof nums2 to access all elements
            lastIndex=lastIndex-1         #keep on decrementing lastIndex value to get all the valid space in nums1
        print(nums1)
        
        
        #this my new version it is more readable and less complex refer to it for code 
    def mergeNew(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            lastIndex=len(nums1)-1
            i=m-1
            j=n-1
            while i>=0 and j>=0:
                if nums1[i]>=nums2[j]:
                    nums1[lastIndex]=nums1[i]
                    lastIndex-=1
                    i-=1
                else :
                    nums1[lastIndex]=nums2[j]
                    lastIndex-=1
                    j-=1
            while j>=0:
                nums1[lastIndex]=nums2[j]
                lastIndex-=1
                j-=1
            print(nums1)
sol=Solution()
sol.merge([0,0,0],0,[2,5,6],3)
sol.mergeNew([0,0,0],0,[2,5,6],3)


        