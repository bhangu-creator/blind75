from typing import Optional

# Definition for a binary tree node.
#ok so this problem is excatly like the same tree problem, the intuation is that we are checking each root node of the root tree with subroot tree since each root of the tree can be 
#classified as its own tree, and wherever we got a match we will return True, the time complexity is O(n*m) where n and m are nodes of respective trees and space is O(h) where h is the height of tree height of recursion stack
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







        