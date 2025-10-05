# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    #ok so intuation is simple if both the nodes are find in 2 different parts of tree i.e left and right then returns the LCA as current root 
    #if both are in same side then just return the first node encountered , the main point to remember is that whatever you return will go to the root of the node
    #so in the end when recusrion is at the root node if only 1 node if found from left and nothing from right then that found node is the LCA , same goes for the right side

    #also just extra observations is that both p and q are also nodes so we can treat each root node as its own tree , so if we received something from left and also from right we know that LCA is the root , but if we only recieve something from left and not from right then it means that lca is the left node and since right is none and vice versa
    #time complexity is O(n) where n is the no of nodes and space is O(h) where h is height of tree for recursion stack
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,p,q):
            if not node:
                return
            if node==p or node==q:
                return node
            leftnode=dfs(node.left,p,q)
            rightnode=dfs(node.right,p,q)
            if leftnode and rightnode:
                return node
            elif not leftnode:
                return rightnode
            else:
                return leftnode
        return dfs(root,p,q)
            