from typing import List


class Solution:
    
    #sort the array first for start time, By doing the sorting of list based on start the whole array will get sorted out. Now imagine a line of numbers from 1 to n where 1 is the start element of the first list and n is the last element of last list. Now try to imagine the interval ranges on that line. There can only be 3 possibilities for intervals on that line. First Possiblity is if there are no overlapping intervals , second is if the two intervals overlap each other like the start of the second interval lies within the range of first interval start and end but the end of the second interval lies outside of range of first interval start and end. In this case we will merge the two intervals such as the merged interval start from start of first interval and and end of merged interval will be the end of second interval. The third case is when the second interval lies within the range of first interval meaning the end of first interval will be greater than or equal to start and end of second interval , in this case we can simply store first interval as merged interval as second interval already is in first so no need to merge
    #time complexity of the following code is On(logn) + O(n) = Onlog(n)
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        retArr=[]
        mergeInt=intervals[0]
        for i in range(1,len(intervals)):
            if mergeInt[1]>=intervals[i][0] :  #this will check if overlap is happening
                if mergeInt[1]<=intervals[i][1]: #this will check if the overlapping interval is totally inside the first interval or the end is outside of first interval
                    mergeInt=[mergeInt[0],intervals[i][1]]   #if the overlapping interval is outside of first then it will merge the two 
            else:
                retArr.append(mergeInt)
                mergeInt=intervals[i]
        retArr.append(mergeInt)
        return retArr   

sol=Solution()
val=sol.merge( [[1,4],[2,3]]) 
print(val)
                    
        