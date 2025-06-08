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
    
    #this iterative way to solve this problem has Time complexity if O(m+n) and space complexity is O(1)
    #it is very similar to merge two sorted arrays but here we first use a dummy list to track the tail pointer
    #we are comparing both the list nodes data and storing the smallest one in the tail pointer and then moving the tail pointer to next position, we will advance the node of the list from which the small node is taken
    #at the end we will check if any of the list is not empty and which one is pending we will basically point the tail pointer to the non empty list since all the nodes in the list are already sorted
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergenode=ListNode(-1)
        tail=mergenode
        while list1 and list2:
            if list1.val<=list2.val:
                tail.next=list1
                tail=tail.next
                list1=list1.next
            else:
                tail.next=list2
                tail=tail.next
                list2=list2.next
        if list1 is not None:
            tail.next=list1
        if list2 is not None:
            tail.next=list2
        return mergenode.next
    
    
    
    #the other way to solve this problem is using recursion , the Time complexity of this solution is O(m+n) since each list is visisted atleast once and Space complexity is O(n+m) since it uses stack becasue of recursion
    #the intuation to solve this problem is that at each recursion we will store the smaller node as left.next and will keep on calling for the next node until one list ends, when 1 of the list ends we will return the opposite list as a base case that is why because rest of the nodes are already sorted and we will then start the merging process from that returned list's head
    #we will keep on merging the smallest nodes at each recursion recall to the returned list in backwards motion and in the end we will have a full merged list and we will return the head
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2     
        if not list2:
            return list1
        if list1.val<=list2.val:
            list1.next=self.mergeTwoLists(list1.next,list2)        #storing the smaller node as list1.next
            return list1
        else:
            list2.next=self.mergeTwoLists(list1,list2.next)        #storing the smaller node as list2.next
            return list2
    
arr=[1, 2, 3, 4, 5]
sol=Solution()
val=createLinkedList(arr)
rev=sol.mergeTwoLists(val)
printList(rev)