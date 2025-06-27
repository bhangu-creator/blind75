from collections import deque

class Node:
    
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
        
    def in_orderDFS(self,node):
        if not node:
            return
        self.in_orderDFS(node.left)
        print(node.val,end="")
        self.in_orderDFS(node.right)
    
    def preorderDFS(self,node):
        if not node:
            return
        print(node.val,end="")
        self.preorderDFS(node.left)
        self.preorderDFS(node.right)
    
    def postorderDFS(self,node):
        if not node:
            return
        self.postorderDFS(node.left)
        self.postorderDFS(node.right)
        print(node.val,end="")
        
    def BFS(self,node):
        if not node:
            return
        queue=deque()
        queue=deque([root])
        while queue:
            curr=queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                          
    def insertNode(self,root,key):
        if root is None:
            return Node(key)
        queue=deque()
        queue=deque([root])
        while queue:
            curr=queue.popleft()
            if not curr.left:
                curr.left=Node(key)
                break
            else:
                queue.append(curr.left)
            if not curr.right:
                curr.right=Node(key)
                break
            else:
                queue.append(curr.right)
        return root
    
    def searchNode(self,root,val):
        if not root:
            return False
        queue=deque()
        queue=deque([root])
        while queue:
            curr=queue.popleft()
            if curr.val==val:
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False
    
    def deleteNode(self,root,val):
        if root is None:
            return None
        queue=deque([root])
        target=None
        while queue:
            curr=queue.popleft()
            if curr.val==val:
                target=curr
                break
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if target is None:
            return root
        
        lastNode=None
        lastParent=None
        queue=deque([(root,None)])
        while queue:
            curr,parent=queue.popleft()
            lastNode=curr
            lastParent=parent
            
            if curr.left:
                queue.append((curr.left,curr))
            if curr.right:
                queue.append((curr.right,curr))
        target.val=lastNode.val
        #remove the lastNode
        if lastParent:
            if lastParent.left==lastNode:
                lastParent.left=None
            else:
                lastParent.right=None
        else:
            return None
        return root
 
        
    def sizeOfTree(self,root):
        if root is None:
            return 0
        count=1
        queue=deque([root])
        while queue:
            curr=queue.popleft()
            if curr.left:
                queue.append(curr.left)
                count+=1
            if curr.right:
                queue.append(curr.right)
                count+=1
        return count
    
    def findLevelofNode(self,root,node):
        if root is None:
            return None
        if root==node:
            return 0
        queue=deque([root])
        level=1
        while queue:
            sizeOfLevel=len(queue)
            for _ in range(sizeOfLevel):
                curr=queue.popleft()
                if curr.left:     
                    if curr.left==node:
                        return level
                    else:
                        queue.append(curr.left)
                if curr.right:
                    if curr.right==node:
                        return level
                    else:
                        queue.append(curr.right)
            level+=1
        return -1
    
    def findHeightofNode(self,root):
        if root is None:
            return None
        queue=deque([root])
        height=0
        while queue:
            sizeOfLevel=len(queue)
            for _ in range(sizeOfLevel):
                curr=queue.popleft()
                if curr.left:     
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            height+=1
        return height
                    
            
        
            
                
        
        
        
        
        
        
        
        
        
root = Node(1)
root = root.insertNode(root, 2)
root = root.insertNode(root, 3)
root = root.insertNode(root, 4)
root = root.insertNode(root, 5)
root = root.insertNode(root, 6)
root = root.insertNode(root, 7)
root.in_orderDFS(root)
print()
root.postorderDFS(root)
print()
root.preorderDFS(root)
print()
root.BFS(root)
print()
val1=root.searchNode(root,10)
val2=root.searchNode(root,4)
print(f"present is {val1}")
print(f"present is {val2}")
print()
root=root.deleteNode(root,3)
root.in_orderDFS(root)
print()
root.postorderDFS(root)
print()
root.preorderDFS(root)
print()
root.BFS(root)
print()
print(root.sizeOfTree(root))
print(root.findHeightofNode(root))
# target_node = root.left.right
# print(root.findLevelofNode(root,target_node))

       
            
        
    