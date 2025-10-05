import heapq

#the main intuation you have to remember is that the in an ordered list , if the list is divided into two parts then the median is the middle of the left side lists's largest num and right hand side's smallest num
#the time complexity is Onlogk and space is O(N)
class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]

    def addNum(self, num: int) -> None:
        maxhp,minhp=self.maxheap,self.minheap
        if not maxhp or num<=-maxhp[0]:
            heapq.heappush(maxhp,-num)
        else:
            heapq.heappush(minhp,num)

        if len(maxhp)>len(minhp)+1:
            maxval=-heapq.heappop(maxhp)
            heapq.heappush(minhp,maxval)
        if len(minhp)>len(maxhp):
            minval=heapq.heappop(minhp)
            heapq.heappush(maxhp,-minval)
        
    def findMedian(self) -> float:
        maxhp,minhp=self.maxheap,self.minheap
        if len(maxhp) == len(minhp):
            return (-maxhp[0] + minhp[0]) / 2
        return -maxhp[0]


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()