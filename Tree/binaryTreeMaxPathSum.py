from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            max_path_left=max(dfs(node.left),0)
            max_path_right=max(dfs(node.right),0)
            self.max_path=max(self.max_path,max_path_left+node.val+max_path_right)
            return max(max_path_left,max_path_right)+node.val

        self.max_path=float('-inf')
        dfs(root)
        return self.max_path
        