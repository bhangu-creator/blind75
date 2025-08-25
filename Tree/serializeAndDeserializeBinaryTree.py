from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        encode_string=""
        queue=deque()
        queue.append(root)
        encode_string=""+str(root.val)
        while queue:
            curr_node=queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
                encode_string+=","+str(curr_node.left.val)
            else:
                encode_string+=","+"None"
            if curr_node.right:
                queue.append(curr_node.right)
                encode_string+=","+str(curr_node.right.val)
            else:
                encode_string+=","+"None"
        return encode_string
            


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="":
            return None
        data_Arr=[]
        word=""
        for ch in data:
            if ch!=',':
                word+=ch
            else:
                if word=="None":
                    data_Arr.append(None)
                else:
                    data_Arr.append(int(word))
                word=""
        queue=deque()
        root=TreeNode(data_Arr[0])
        queue.append(root)
        n=len(data_Arr)
        indx=1
        while queue:
            curr_node=queue.popleft()
            if indx<n and data_Arr[indx]!=None:
                left=TreeNode(data_Arr[indx])
                curr_node.left=left
                queue.append(left)
            indx+=1
            if indx<n and data_Arr[indx]!=None:
                right=TreeNode(data_Arr[indx])
                curr_node.right=right
                queue.append(right)
            indx+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))




#USING DSF:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        encode_string=""
        def dfs(node,encode_string):
            if node is None:
                encode_string+="N,"
                return encode_string
            encode_string+=str(node.val)+","
            encode_string=dfs(node.left,encode_string)
            encode_string=dfs(node.right,encode_string)
            return encode_string

        return dfs(root,encode_string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="":
            return None
        word=""
        data_Arr=[]
        for ch in data:
            if ch!=",":
                word+=ch
            else:
                if word=="N":
                    data_Arr.append(None)
                else:
                    data_Arr.append(int(word))
                word=""

        def dfs(data_Arr,n):
            if self.indx>n or data_Arr[self.indx] is None:
                self.indx+=1
                return None
            print(self.indx)
            root=TreeNode(data_Arr[self.indx])
            self.indx+=1
            root.left=dfs(data_Arr,n) 
            root.right=dfs(data_Arr,n) 
            return root
        n=len(data_Arr)
        self.indx=0
        return dfs(data_Arr,n)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))