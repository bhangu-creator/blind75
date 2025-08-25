from collections import defaultdict
from typing import List
import heapq
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue=deque()
        queue.append(root)
        while queue:
            curr_node=queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
                left=curr_node.left
            if curr_node.right:
                queue.append(curr_node.right)
                right=curr_node.right
            curr_node.left,curr_node.right=right,left
        return root
        




                  
sol=Solution()
res=sol.invertTree([4,2,7,1,3,6,9])
print(res)








