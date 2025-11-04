# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good=0
        def dfs(node,maxval):
            if node is None:
                return
            if node.val>=maxval:
                self.good+=1
                dfs(node.left,node.val)
                dfs(node.right,node.val)
            else:       
                dfs(node.left,maxval)
                dfs(node.right,maxval)        
        dfs(root,root.val)
        return self.good
        