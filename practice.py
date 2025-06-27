from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def printTreeLevelOrder(self,root):
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid=True
        if root is None:
            return False
        queue=deque([root])
        rootVal=root.val
        while queue:
            curr=queue.popleft()
            if curr.left:
                if curr.left.val>=curr.val and curr.left.val>=rootVal:
                    return False
                else:
                    queue.append(curr.left)
            if curr.right:
                if curr.right.val<=curr.val and curr.right.val<=rootVal:
                    return False
                else:
                    queue.append(curr.right)
        return True




sol=Solution()
firstNode=TreeNode(5)
secondNode=TreeNode(4)
thirdNode=TreeNode(6)
fourthNode=TreeNode(3)
fifthNode=TreeNode(7)
# sixthNode=TreeNode(6)
# seventhNode=TreeNode(9)
firstNode.left=secondNode
firstNode.right=thirdNode
# secondNode.left=fourthNode
# secondNode.right=fifthNode
thirdNode.left=fourthNode
thirdNode.right=fifthNode
sol.printTreeLevelOrder(firstNode)
validy=sol.isValidBST(firstNode)
print(validy)
sol.printTreeLevelOrder(firstNode)
        
            


            
        

sol=Solution()
val=sol.minWindow("aa","aa")
print(val)
        
        