from  collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(node):
            queue=deque()
            queue.append((node,0))
            max_width=1
            while queue: 
                for _ in range(len(queue)):
                    curr_node,curr_width=queue.popleft()
                    if curr_node.left:
                        queue.append((curr_node.left,(2*curr_width)+1))
                    if curr_node.right:
                        queue.append((curr_node.right,(2*curr_width)+2))
                if queue:
                    left,right=queue[0][1],queue[-1][1]
                    total_width=(right-left)+1
                    max_width=max(max_width,total_width)
            return max_width
        return bfs(root)
            

        