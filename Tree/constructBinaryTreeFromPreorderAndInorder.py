
from typing import List
from typing import Optional
# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndexMap={ val: idx for idx, val in enumerate(inorder)}
        self.preorder_index=0
        def build(left,right):
            if left>=right:
                return None
            root_val=preorder[self.preorder_index]
            self.preorder_index+=1
            root=TreeNode(root_val)
            inorder_index=inorderIndexMap[root_val]
            root.left=build(left,inorder_index)
            root.right=build(inorder_index+1,right)
            return root
        return build(0,len(inorder))
    
preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
sol=Solution()
sol.buildTree(preorder,inorder)



