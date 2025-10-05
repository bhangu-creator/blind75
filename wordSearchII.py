
from typing import List

class TrieNode():
    def __init__(self):
        self.children={}
        self.isEnd=False

class Solution:

    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.isEnd=True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        Row=len(board)
        Col=len(board[0])
        visited=[[False for _ in range(Col)] for _ in range(Row)]
        directions=[(0,1),(-1,0),(0,-1),(1,0)]
        result=[]

        for word in words:
            self.insert(word)

        def isValid(row,col):
            if row<0 or row>=Row or col<0 or col>=Col or visited[row][col]:
                return False
            return True

        def dfs(row,col,node,res):
            visited[row][col]=True
            if node.isEnd:
                node.isEnd=False
                result.append("".join(res))

            for r,c in directions:
                adjx=row+r
                adjy=col+c
                if isValid(adjx,adjy):
                    if board[adjx][adjy] in node.children:
                        char=board[adjx][adjy]
                        res.append(char)
                        dfs(adjx,adjy,node.children[char],res)
                        res.pop()

            visited[row][col]=False
        node=self.root
        for row in range(Row):
            for col in range(Col):
                if board[row][col] in node.children:
                    res=[]
                    res.append(board[row][col])
                    dfs(row,col,node.children[board[row][col]],res)     
        return result
        
#ok so intuation for this problem is that we can use a trie for this problem to optimally look up
#all the possible words available. just use matrix directions to explore all adjacent paths and if the char exist in trie go there if it does not 
#then just come back. this way we can explore all thepaths
#time complexity is O(m*n*l) where l is average length of all the words
#space is O(W*L) where W is no of all the words and L is average length of all the words
