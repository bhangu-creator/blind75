from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #a link list is basically a left skwered binary tree , we can only move forwards in link list so we have to build this tree from left side first and then root and then right side
    #just keep on crrating nodes at each recursive step and we will be doing this from the far end of left side of tree and since list is sorted we will eventually get the BST
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.head=head
        fast=head
        length=0
        while fast:
            fast=fast.next
            length+=1
        def build(left,right):
            if left>=right:
                return None
            mid=(left+right)//2
            leftChild=build(left,mid)
            root=TreeNode(self.head.val)
            self.head=self.head.next
            rightChild=build(mid+1,right)
            root.left=leftChild
            root.right=rightChild
            return root
        return build(0,length)
        
head = [-10,-3,0,5,9]
sol=Solution()
sol.sortedListToBST(head)