from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result,prev,curr=set(),set(),set()
        for indx in range(len(arr)):
            for elem in prev:
                curr.add(arr[indx]|elem)
                result.add(arr[indx]|elem)
            curr.add(arr[indx])
            result.add(arr[indx])
            prev=curr.copy()
            curr.clear()
        return len(result)
