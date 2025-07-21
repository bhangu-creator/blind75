from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def bfs(node):
            queue=deque()
            queue.append(node)
            count=0
            while queue:
                len_q=len(queue)
                for _  in range(len_q):
                    curr=queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                count+=1
            return count
        return bfs(root)
    
#DFS solution , basically travserse to the last node and keep on adding +1 to the left node and right and return the max of both

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            return 1+ max(left,right)
        return dfs(root)
                
        