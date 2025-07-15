# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
#     initialize a int variable as res=0
# loop through whole linked list to get value from each node
# while doing that first left shift the res variable to make space for new bit to be added
# after doing that use OR operator to add the bit from node's value in the res
# return res, since it's an int type it will return the decimal value
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res=0
        while head:
            res=res<<1
            res=res|head.val
            head=head.next
        return res
#there are many other intuations of doing this , go check leetcode submissions you will remember
