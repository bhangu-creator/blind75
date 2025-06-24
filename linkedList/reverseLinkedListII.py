from typing import Optional




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    #the intuation for this problem is very raw
    #we basically reversing a link list but we are doing this in the middle of another list
    #first loop is used to get the head of the link list part from which we need to reverse the string and also get the previous node of that left to do the inplace reverse
    #second loop is our standard reverse a singly link list code
    #basically the most important part comes after this loop, what happens is acually when we reverse the list the end point and the front point of that list are also reversed so we manually have to attach them to their correct endpoints
    #that is why before entering the second loop we first store the head of the list to be reversed and its previous node as we had to attach them properly after the process is completed,
    # pls look at notes in notebooks and draw the example visually
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        slow=dummy
        for _ in range(left):
            prev=slow
            slow=slow.next
        firstNode=slow
        previous=prev
        for _ in range(right-left+1):
            forward=slow.next
            slow.next=prev
            prev=slow
            slow=forward
        firstNode.next=slow    #most important part
        previous.next=prev     #most important part
        return dummy.next



        

        
        








        