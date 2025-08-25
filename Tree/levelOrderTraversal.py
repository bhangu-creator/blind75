from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        if not root:
            return []
        retArr=[]
        queue=deque()
        queue.append(root)
        while queue:
            sizeOfQueue=len(queue)
            level_list=[]
            for _ in range(sizeOfQueue):
                curr_node=queue.popleft()
                level_list.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            retArr.append(level_list)
        return retArr

        