from collections import defaultdict 

class TimeMap:

    def __init__(self):
        self.timestore=defaultdict(dict)
        self.keystore=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        store=self.timestore
        keys=self.keystore
        store[key][timestamp]=value
        keys[key].append(timestamp)

        
    def get(self, key: str, timestamp: int) -> str:
        store=self.timestore
        keys=self.keystore
        shop=store[key]
        if timestamp in shop:
            return shop[timestamp]
        keyArr=keys[key]
        left,right=0,len(keyArr)-1
        res=-1
        while left<=right:
            mid=(left+right)//2
            if keyArr[mid]>timestamp:
                right=mid-1
            else:
                res=mid
                left=mid+1
        if res==-1:
            return ""
        return shop[keyArr[res]]

#time is o(logn) binary search and space is O(n)
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)