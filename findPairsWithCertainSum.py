from typing import List
from collections import Counter

class FindSumPairs:

    #intuation is very simple we know the target val and we know nums1+num2=val so nums2=val-nums1
    #we use freq_map to count how many pairs are possible and whenever we increase a element by a certain value we modify freq_map_nums2 also if it was the only element means freq was 1 and then it will become 0 and we will delete the num other wise we will just decrease the freq anyway and add new value in nums2 dict

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2
        self.freq_map_nums1=Counter(self.nums1)
        self.freq_map_nums2=Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        oldval=self.nums2[index]
        newval=oldval+val
        self.nums2[index]=newval
        self.freq_map_nums2[oldval]-=1
        if self.freq_map_nums2[oldval]==0:
            del self.freq_map_nums2[oldval]
        self.freq_map_nums2[newval]+=1
        
    def count(self, tot: int) -> int:
        count=0
        for num,freq in self.freq_map_nums1.items():
            if tot-num in self.freq_map_nums2:
                count+=freq*self.freq_map_nums2[tot-num]
        return count
        


# Your FindSumPairs object will be instantiated and called as such:
nums1=[1, 1, 2, 2, 2, 3]
nums2=[1, 4, 5, 2, 5, 4]
val=3
index=3
tot=7
obj = FindSumPairs(nums1, nums2)
obj.add(index,val)
param_2 = obj.count(tot)
print(param_2)