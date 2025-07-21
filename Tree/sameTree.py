from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if p and q:
                if p.val!=q.val:
                    return False
            elif not p and not q:
                return True
            else:
                return False
            if not dfs(p.left,q.left):
                return False
            if not dfs(p.right,q.right):
                return False
            return True
            
        return dfs(p,q)
    #using bfs
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(p,q):
            queue=deque()
            queue.append([p,q])
            while queue:
                tree1,tree2=queue.popleft()
                if tree1 and tree2:
                    if tree1.val!=tree2.val:
                        return False
                    queue.append([tree1.left,tree2.left])
                    queue.append([tree1.right,tree2.right])
                elif not tree1 and not tree2:
                    continue
                else:
                    return False
            return True
        return bfs(p,q)

        