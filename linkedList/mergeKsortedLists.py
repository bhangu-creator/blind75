from typing import Optional
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    
    #this solution is the extension of the merge two sorted list solution, if you notice in this the mergetwolist is literaly the same method used in that problem
    #the mergedl list it returns is then used to merge the rest of the lists in the array
    #this solution's time complexity is O(n*k) where n is the total number of nodes in the array and k is the total no of link lists in the array, the for loop runs for k-1 times and the mergetwolists method is called for n nodes n times so the time complexity becomes this
    #this solution's space complexity is O(1) which is optimal
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        dummy=ListNode(-1)
        def mergetwolists(node1,node2):
            tail=dummy
            while node1 and node2:
                if node1.val<=node2.val:
                    tail.next=node1
                    tail=tail.next
                    node1=node1.next
                else:
                    tail.next=node2
                    tail=tail.next
                    node2=node2.next
            if node1:
                tail.next=node1
            if node2:
                tail.next=node2
            return dummy.next
        mergenode=lists[0]
        for i in range(1,len(lists)):
            mergenode=mergetwolists(mergenode,lists[i])
        return mergenode
    
    #this solution can be made more optimal by using merge sort or heap 
    #we will for now use merge sort that will reduce its time complexity to O(nlogk) which is optimal and space complexity is O(log k) due to recursion stack(divide and conquer spliting)
    #here first we created a method called split lists , which will split the list till there is only 1 list is left in array and when that happends we will return that list
    #till that we will keep on slitting the list using mid 
    
    def mergeKListsByMergeSort(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        def merge(node1,node2):
            dummy=ListNode(-1)
            tail=dummy
            while node1 and node2:
                if node1.val<=node2.val:
                    tail.next=node1
                    tail=tail.next
                    node1=node1.next
                else:
                    tail.next=node2
                    tail=tail.next
                    node2=node2.next
            if node1:
                tail.next=node1
            if node2:
                tail.next=node2
            return dummy.next

        def splitLists(left,right,lists):
            if left==right:
                return lists[left]
            mid=(left+right)//2
            node1=splitLists(left,mid,lists)  #imagine it is 0,0,lists (here node1 will be the list at index 0 of array)
            node2=splitLists(mid+1,right,lists)  #same here in end there will be 1,1,lists (here node2 will be the list at index 1 of array)
            return merge(node1,node2)  #so here we will merge those two lists and return the new merged list to  splitLists(0,1) and so on....

        return splitLists(0,len(lists)-1,lists)
    
    
    def build_linked_lists(self,arrays):
        result = []
        for lst in arrays:
            dummy = ListNode(-1)
            curr = dummy
        for num in lst:
            curr.next = ListNode(num)
            curr = curr.next
        result.append(dummy.next)  # head of the current list
        return result
    
    def print_linked_list(self,head):
        while head:
            print(head.val, end=" -> " if head.next else "\n")
            head = head.next

    
input_data = [[1,4,5],[1,3,4],[2,6]]
sol=Solution()
lists = sol.build_linked_lists(input_data)
head=sol.mergeKListsByMergeSort(lists)
sol.print_linked_list(head)


        