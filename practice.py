from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        intervalArr=[]
        for interval in range(0,len(intervals)):
            if intervals[interval+1][0][1]<=intervals[interval][1] and intervals[interval+1][0][1]<=intervals[interval][0]:
                intervalArr.append([intervals[interval][0],[intervals[interval][1]]])
            elif interval[intervals+1][0]<=interval[interval][1]:
                intervalArr.append([[interval[intervals][0],interval[intervals+1][1]]])
            else:
                intervalArr.append([[interval]])
        return intervalArr
            

        


sol=Solution()
val=sol.productExceptSelf([1,2,3,4])
print(val)












