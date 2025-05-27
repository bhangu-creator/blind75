
#This is the merge sort algorithm

class Sorting:

    def merge(self,arr,left,mid,right):
        leftArr=arr[left:mid+1]
        rightArr=arr[mid+1:right+1]
        k=left
        i=j=0
        while i<len(leftArr) and j<len(rightArr):
            if leftArr[i]<rightArr[j]:
                arr[k]=leftArr[i]
                i=i+1
            else:
                arr[k]=rightArr[j]
                j=j+1
            k=k+1
        while i<len(leftArr):
                arr[k]=leftArr[i]
                k=k+1
                i=i+1
        while j<len(rightArr):
                arr[k]=rightArr[j]
                k=k+1
                j=j+1

    def mergeSort(self,arr,left,right):
        if left<right:
            mid=(left+right)//2
            self.mergeSort(arr,left,mid)
            self.mergeSort(arr,mid+1,right)
            self.merge(arr,left,mid,right)
            
sort = Sorting()
n=[5,2,1,9,8,10,3,7,8,8]
sort.mergeSort(n,0,len(n)-1)
print(n)
