
from typing import List
from typing import Optional
# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #the intuation is :
    #preorder is : Root->Left->Right, given this we can say that each element of preorder array's is a root to its subtree, so we now already know the root nodes of tree .
    #inorder is : Left->Root->Right, given this if we pick the root from preorder and search it in inorder than we can say that all the elements to left of that element are going to be in its left subree and all the right are going to be in right subtree
    #so if we do this recursively and just created a root node at each recursion and then attach it to left and right on backtracking we will get the binary tree
    #node : we can construct a unique tree always if inorder traversal is given with preorder or postorder

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndexMap={ val: idx for idx, val in enumerate(inorder)}
        self.preorder_index=0
        def build(left,right):
            if left>=right:
                return None
            root_val=preorder[self.preorder_index]
            self.preorder_index+=1
            root=TreeNode(root_val)
            inorder_index=inorderIndexMap[root_val]
            root.left=build(left,inorder_index)
            root.right=build(inorder_index+1,right)
            return root
        return build(0,len(inorder))
    
preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
sol=Solution()
sol.buildTree(preorder,inorder)



