from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    #the intuation is :
    #postorder is : Left->Right->Root, given this we can say that each element of postorder array's from back is a root to its subtree, so we now already know the root nodes of tree .
    #inorder is : Left->Root->Right, given this if we pick the root from postorder and search it in inorder than we can say that all the elements to left of that element are going to be in its left subree and all the right are going to be in right subtree
    #in this we will first create the tree from right then root and then left, doing this recursively will give us binary tree
    #node : we can construct a unique tree always if inorder traversal is given with preorder or postorder
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIndexMap= {val:idx for idx,val in enumerate(inorder)}
        self.rootIndex=len(postorder)-1
        def build(left,right):
            if left>=right:
                return None
            rootVal=postorder[self.rootIndex]
            self.rootIndex-=1
            root=TreeNode(rootVal)
            inorderIndex=inorderIndexMap[rootVal]
            root.right=build(inorderIndex+1,right)
            root.left=build(left,inorderIndex)
            return root
        return build(0,len(inorder))
        
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
sol=Solution()
sol.buildTree(inorder,postorder)