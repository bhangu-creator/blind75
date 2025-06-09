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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    #first method - Two Pass
    #problem is since n is from back we need to find the length of list first
    #After finding the length  of the link list then subtract the length from n to get index 1 before the actual one we need to remove and then we can perform the action
    #need two more if blocks to handle the edge cases of n being on first position / last position and link list with only 1 node
    #why this solution not optimal?:
    #1 it requires two loops to pass from list 2 times which is O(n) + O(n)
    #it is not clean
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currentnode=head
        tempnode=head
        index=count=0
        while currentnode:
            currentnode=currentnode.next
            index+=1
        if index==n:    #this handles the Test cases of linklist with 1 node and n=1 AND also if the n is the head of the list
            return head.next
        removeIndex=index-n
        while tempnode and count+1!=removeIndex :
            tempnode=tempnode.next
            count+=1
        if tempnode.next:
            tempnode.next=tempnode.next.next        
            return head
        
        
        #to make the above approach more eficent we have now used 2 pointer technique here , 
        #the core intuation is that if we initialize two pointers , fast and slow, and if we moved fast n+1 steps ahead then slow pointer is always land on 1 node before the node we want to remove and also there is always gonna be n+1 steps gap between slow and fast if we then move them together, so if fast then reaches at any point the end then the slow is going to be at a node just before the node that we need to replace
        #we used fast=slow=dummy here as because of dummy the pointers will start before the first node and also fast will finish at the null node this makes the edge cases much easier to handle like if n==length of the list or if there is only 1 node in the list, in both these cases we just need to move head 1 node ahead
    def removeNthFromEndTwoPointers(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        slow=fast=dummy
        for _ in range(n+1):      #first used the loop to make fast jump n steps ahead
            if fast:
                fast=fast.next
        while fast:               #from now on when we move fast and slow together there will always be n steps gap between them
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next     #when the loop ends the slow pointer will be at the node just before the node that we have to remove
        return dummy.next            #return the dummy.next as that is where our head is stored
    
        

arr=[1,2,3]
sol=Solution()
val=createLinkedList(arr)
rev=sol.removeNthFromEndTwoPointers(val,3)
printList(rev)