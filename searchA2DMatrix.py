from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row=len(matrix)
        Col=len(matrix[0])

        def isPresent(row,Col):
            left,right=0,Col-1
            while left<=right:
                mid=(left+right)//2
                if target==matrix[row][mid]:
                    return True
                elif target>matrix[row][mid]:
                    left=mid+1
                else:
                    right=mid-1
            return False

        for row in range(Row):
            if  isPresent(row,Col):
                return True            
        return False
#think of it as like searching m rows in logn time so time complexity is O(m*logn)