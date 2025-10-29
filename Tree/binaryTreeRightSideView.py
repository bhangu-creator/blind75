# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from typing import Optional
from collections import  deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        result=[]
        while queue:
            size=len(queue)
            result.append(queue[-1].val)
            for _ in range(size):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

#the intuation is that each level you stand at the right side and view the first node that you could view from that side
#O(N) space and O(N) Time where N is no of nodes present in tree
        