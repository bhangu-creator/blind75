from typing import List;
import random;
import heapq;

#this problem can be done using priority queue and also using quickselect , the following code is of quickselect. 
#the avg time complexity is O(n)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        listOfPoints=[]
        for point in points:
            x,y=point[0],point[1]
            val=((x*x) + (y*y))**0.5
            listOfPoints.append((point,val))

        def findPivot(left,right,pivotIndx):
            pivot=listOfPoints[pivotIndx][1]
            listOfPoints[pivotIndx],listOfPoints[right]=listOfPoints[right],listOfPoints[pivotIndx]
            start=left
            for indx in range(left,right):
                if listOfPoints[indx][1]<pivot:
                    listOfPoints[indx],listOfPoints[start]=listOfPoints[start],listOfPoints[indx]
                    start+=1
            listOfPoints[start],listOfPoints[right]=listOfPoints[right],listOfPoints[start]
            return start
        
        def partition(left,right):
            pivot=random.randint(left,right)
            pivot=findPivot(left,right,pivot)
            if pivot==k-1:
                return pivot
            elif pivot>=k:
                right=pivot-1
            else:
                left=pivot+1
            return partition(left,right)

        pivot=partition(0,len(listOfPoints)-1)
        res=[]
        for point,value in listOfPoints:
            res.append(point)
            if len(res)==pivot+1:
                break
        return res

#the folllowing is the priority queue solution

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[(float('-inf'),[float('-inf'),float('-inf')])] * k
        for indx in range (len(points)):
            dist=-((points[indx][0]**2)+ (points[indx][1]**2))**0.5
            heapq.heappush(heap,(dist,points[indx]))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for dist,point in heap:
            res.append(point)
        return res