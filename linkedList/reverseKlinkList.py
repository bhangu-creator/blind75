# Definition for singly-linked list.
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

#intuation is simple we had to do this in O(n) time and O(1) space. 
#first thing we did is just to calculate the length of list and then just compute how many pieces list will be split to call the method that many times
#the second thing is just create a helper method to reverse a list for only for k nodes
#the third thing we did is just rettach all the pieces together to make a full list to return

from typing import Optional;
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        fast=head
        while fast:
            length+=1
            fast=fast.next
        if length<k:
            return head
        piece=length//k

        def reversenodes(node):
            indx=0
            prev=None
            currentnode=node
            lastnode=node
            while indx<k and currentnode:
                forward=currentnode.next
                currentnode.next=prev
                prev=currentnode
                currentnode=forward
                indx+=1
            return prev,currentnode,lastnode

        count=0
        currenthead=head
        mainhead=None

        tail=ListNode(-1)
        while count<piece:
            newhead,forward,tailnode=reversenodes(currenthead)
            if not mainhead:
                mainhead=newhead
            tail.next=newhead
            tail=tailnode
            currenthead=forward
            count+=1
        if currenthead:
            tail.next=currenthead
        return mainhead

            

        