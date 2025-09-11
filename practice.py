from collections import defaultdict
from typing import List
import heapq
from collections import deque
from typing import Optional

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        down=True
        retArr=[]
        Row=len(mat)
        Col=len(mat[0])
        row,col=0,0
        retArr.append(mat[row][col])
        while row!=Row-1 and col!=Col-1:
            if down:
                col+=1
                while True:
                    retArr.append(mat[row][col])
                    if col==0:
                        break
                    row+=1
                    col-=1
                down=False
            else:
                row+=1
                while True:
                    retArr.append(mat[row][col])
                    if row==0:
                        break
                    row-=1
                    col+=1
                down=True
        retArr.append(mat[row][col])
        return retArr

    

sol=Solution()
sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])




                  
sol=Solution()
res=sol.invertTree([4,2,7,1,3,6,9])
print(res)








