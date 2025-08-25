from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root,subroot):
            if not root and not subroot:
                return True
            elif root and subroot:
                if root.val!=subroot.val:
                    return False
                if not isSameTree(root.left,subroot.left):
                    return False
                if not isSameTree(root.right,subroot.right):
                    return False
            else:
                return False
            return True
        def dfs(root,subroot):
            if not root:
                return 
            if root.val==subroot.val:
                if isSameTree(root,subroot):
                    return True
            if dfs(root.left,subroot):
                return True
            if dfs(root.right,subroot):
                return True
            return False

        if dfs(root,subRoot):
            return True
        return False







        