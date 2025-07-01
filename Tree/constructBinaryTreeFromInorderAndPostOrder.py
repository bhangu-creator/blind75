from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIndexMap= {val:idx for idx,val in enumerate(inorder)}
        self.rootIndex=len(postorder)-1
        def build(left,right):
            if left>=right:
                return None
            rootVal=postorder[self.rootIndex]
            self.rootIndex-=1
            root=TreeNode(rootVal)
            inorderIndex=inorderIndexMap[rootVal]
            root.right=build(inorderIndex+1,right)
            root.left=build(left,inorderIndex)
            return root
        return build(0,len(inorder))
        
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
sol=Solution()
sol.buildTree(inorder,postorder)