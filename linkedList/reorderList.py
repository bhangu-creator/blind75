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
    
    #this approach uses stack 
    #the first loop in this code is going to get the length of the list
    #after getting the length we will find the mid of the list
    #then we will initialize a stack and then we will start a new loop 
    #the purpose of the new loop is to get to mid first and after getting to mid we will start getting all the nodes after the mid of list in the stack
    #we are using stack for this operation as it is the datastructure that follows first in last out , that way we will get all the nodes after mid of the list in reverse order which is needed for this problem
    #now after putting all the 2nd half nodes in the stack, the loop will end when list reaches its end
    #now we will start a new loop which will be used to link the nodes of the original list to the nodes stored in the stack
    #when we reorder the list as the problem demands than we will point the last node to null which will ensure that our new reorderd list is valid
    
    #take a look at submissiono at 20-06-2025 on leetcode, optimal version is present
    def reorderList(self, head: Optional[ListNode]) -> None:
        length=0
        tempnode=head
        while tempnode.next:
            tempnode=tempnode.next
            length+=1
        pivot=length//2
        stack=[]
        tempnode2=head
        count=0
        while tempnode2:
            if count>pivot:
                stack.append(tempnode2)
            tempnode2=tempnode2.next
            count+=1
        reordernode=head
        while reordernode and reordernode.next and stack:
            forward=reordernode.next
            nodefromstack=stack.pop()
            reordernode.next=nodefromstack
            nodefromstack.next=forward
            reordernode=forward
        if reordernode:
            reordernode.next = None
        
        
        
        #this approach is two pointer approach
        #in this approach we will first use two pointers fast and slow to get the mid node of the list
        #fast pointer will move 2 steps ahead while slow moves only 1 step , this way when fast reaches the end the slow pointer will be at the mid node
        #now we will have two pointers one is the original head pointer of the list starting from start to end and the other is mid pointer start from mid to end
        #now we will again use a while loop to revserse the 2nd list which starts from mid to end 
        #now when the 2nd list from mid to last gets reversed we can again use a while loop to traverse both the lists till they reaches there end and will keep on reorder the nodes inside the loop
        #when the loop ends we will point the last node of head to null to ensure the list closes valid
    def reorderListTwoPointers(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        previous=None
        secondHalf=slow
        while secondHalf:
            forward=secondHalf.next
            secondHalf.next=previous
            previous=secondHalf
            secondHalf=forward
        secHalf=previous
        firstHalf=head
        while firstHalf and firstHalf.next and secHalf:
            fwdnode=firstHalf.next
            firstHalf.next=secHalf
            tempsec=secHalf.next
            secHalf.next=fwdnode
            secHalf=tempsec
            firstHalf=fwdnode
        if firstHalf:
            firstHalf.next=None
            
            
            
        #ignore this code as it is used to print the value
        current_node=head
        while(current_node):
            print(current_node.val, end=" -> " if current_node.next else "\n")
            current_node=current_node.next
            
            

arr=[1,2,3,4]
sol=Solution()
val=createLinkedList(arr)
sol.reorderListTwoPointers(val)
# printList(rev)