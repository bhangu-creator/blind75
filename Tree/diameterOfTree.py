# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxpath=float('-inf')
        
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            self.maxpath=max(self.maxpath,left+right)
            return max(left+1,right+1)
        dfs(root)
        return self.maxpath

#the intuation is max path can means max edges connected with root from left and right. so for every root we will store the 
#max edges we get from left and we get from right and we will add them and store there max and will send only 1 path above that will be max of left+1 or right+1
#time and space complexity is O(n) and O(h)
            