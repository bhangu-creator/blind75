
from typing import Optional

def createLinkedList(arr):   #this is just a helper method to convert array lists to link list
     if not arr:
         return None
     head = ListNode(arr[0])
     current = head
     for val in arr[1:]:
         current.next = ListNode(val)
         current = current.next
     return head
 
def printList(head):           #this method is just used to print the values of linklist
        current_node=head
        while(current_node):
            print(current_node.val, end=" -> " if current_node.next else "\n")
            current_node=current_node.next



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #this problem is solved using the slow and fast pointer method, both slow and fast pointer will start from the head but the slow pointer will move 1 step while the head pointer will move 2 step.
    #eventually if the link list has cycle meaning if we traverse the loop it will run for infinity , in that case there will come a point when faster pointer will have traverse the whole list and will meet the slow pointer again, when that Happens we will return True
    #if the loop ends that would mean there is None pointer in list meaning it has no cycle
    #just a fact that : when fast reaches end of list the slow will be at exact the mid of list
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow=head
        fast=head.next
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False


arr=[1, 2, 3, 4, 5]
sol=Solution()
val=createLinkedList(arr) #will not create a cycel link list
rev=sol.hasCycle(val)
printList(rev)