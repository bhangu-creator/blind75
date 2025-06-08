
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

class ListNode:              #this is just a node class
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    #the intiuation to solve this problem is to not think of link lists as array where as in array if you want to reverse it you will have to rearrange the elements
    #but in link list that can be achieved without changing the position of nodes by just simply manupulationg or reversing the next pointers of each node
    #if you can imagine if we just reverse the next pointer of each node that way the last node will become head and first node will become the last node as it will point to none pointer
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         
        currentNode=head   #initialzed a temporary node
        previousNode=None  #initialized the previous node as None because as first node will be the last  node after reverse than that node will be pointing to the None
        
        while currentNode is not None:   #while we do not get  a invalid node
            forwardNode=currentNode.next     #we first store the next pointer that point towards the next node so that we can trasverse the loop if we changed the next pointer of the current node
            currentNode.next=previousNode    #we changed the next pointer of the current node to previous node which was null making the next pointer of first node of list null
            previousNode=currentNode         #we then made the previous node the current node so that we can use it in next iteration
            currentNode=forwardNode          #we made the current node to the forward node so that we can repeat the same process again
        return previousNode                  #return the head of the previous node as it will be the first node of list when the loop ends 
    
    #the below solution is using the recursion method
    #the intiuation to solve this problem using recursion is that we observe the last node of the list will be the first node of the reverse list , so if we access that node somehow and make it our head node and then keep on traversing backwards and just reversing the links we will get the reverse link list
    #we will keep on calling the recursive method for each node
    #the base case for this recursion is when there is only 1 node is left that is the last node and it will return that node 
    #it will return the last node with null pointer to the 2nd last call e.x 4 , here we just need to swap the head.next.next node with head and then assign head as None and then again return the new head which will be same for all iterations 
    def reverseListUsingRecursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newHead=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newHead
    
    

arr=[1, 2, 3, 4, 5]
sol=Solution()
val=createLinkedList(arr)
rev=sol.reverseList(val)
printList(rev)

        