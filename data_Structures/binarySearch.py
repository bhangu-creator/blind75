#this is the binary search algorithm

class Search:
    
    #This approach is called iterative approach
    def binarySearch(self,arr,left,right,x):
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==x:
                return True
            elif arr[mid]<x:
                left=mid+1
            else:
                right=mid-1
        return False
    
    #This approach is called reccursive approach
    def binarySearchRec(self,arr,left,right,x):
          while left<=right:
            mid=(left+right)//2
            if arr[mid]==x:
                return True
            elif arr[mid]<x:
                return self.binarySearchRec(arr,mid+1,right,x)
            else:
                 return self.binarySearchRec(arr,left,mid-1,x)
          return False
        
    
sar = Search()
n=[1,4,12,16,19,22,25]
fnd=sar.binarySearchRec(n,0,len(n)-1,25)
print(fnd)


        
        