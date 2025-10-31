# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            if left==-1 or right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return max(1+left,1+right)
        res=dfs(root)
        if res==-1:
            return False
        return True
    
#height of tree is the max path from to the root either from left or right
#time and space isO(n) and O(h)


            
            
        