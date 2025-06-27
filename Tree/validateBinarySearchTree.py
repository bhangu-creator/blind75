
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def isValid(self,root,minVal,maxVal):
        if root is None:
            return True
        if minVal<root.val<maxVal:
            return self.isValid(root.left,minVal,root.val) and self.isValid(root.right,root.val,maxVal)
        return False
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal=float('-inf')
        maxVal=float('inf')
        return self.isValid(root,minVal,maxVal)
    
    #bsf here:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal=float('-inf')
        maxVal=float('inf')
        queue=deque([(root,minVal,maxVal)])
        while queue:
            curr,minVal,maxVal=queue.popleft()
            if minVal<curr.val<maxVal:
                if curr.left:
                    queue.append((curr.left,minVal,curr.val))
                if curr.right:
                    queue.append((curr.right,curr.val,maxVal))
            else:
                return False
        return True

