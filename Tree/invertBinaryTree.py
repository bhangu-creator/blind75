# Definition for a binary tree node.

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


#inituation for iterative way is that to swap the nodes at each level since binary tree only have atleast 2 nodes at each level so we can simply swap the two
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue=deque([root])
        while queue:
            curr=queue.popleft()
            curr.left,curr.right=curr.right,curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root
    
    #this is the approach using inorder dfs 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root

sol=Solution()
firstNode=TreeNode(4)
secondNode=TreeNode(2)
thirdNode=TreeNode(7)
fourthNode=TreeNode(1)
fifthNode=TreeNode(3)
sixthNode=TreeNode(6)
seventhNode=TreeNode(9)
firstNode.left=secondNode
firstNode.right=thirdNode
secondNode.left=fourthNode
secondNode.right=fifthNode
thirdNode.left=sixthNode
thirdNode.right=seventhNode
root=sol.invertTree(firstNode)
sol.printTreeLevelOrder(root)






                

        