from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #intuation is very simple since BST has less than root values on left side and greater than root value on right side , and given array is sorted so we can split the array from half and then attach the left elements to left side and right elements to right side of tree 
    #do this recursively and we will get the BST
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left,right):
            if left>=right:
                return None
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=build(left,mid)
            root.right=build(mid+1,right)
            return root
        return build(0,len(nums))
        
nums = [-10,-3,0,5,9]
sol=Solution()
sol.sortedArrayToBST(nums)