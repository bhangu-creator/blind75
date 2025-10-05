# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter=0
        self.val=0
        def dfs(node):
            if node is None:
                return False
            if dfs(node.left):
                return True
            self.counter+=1
            if self.counter==k:
                self.val=node.val
                return True
            return dfs(node.right)

        dfs(root)
        return self.val
    
#given the property of BST the left most node has smallest value and the right most node has the largest value
#so using inorder traversal we can get all the nodes in sorting order and just return recursion when at kth node
#the time complexity is O(N) and space is also O(N)


            
                