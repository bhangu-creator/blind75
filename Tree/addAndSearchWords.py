
#intuation is simple, understand how tries work and this will be easy
#time complexity for addword is O(L) where L is the length of the word to be inserted , since we go through each character one by one
#time complexity for search if no dots are present is O(L) same logic as above, but if there are D dots then it becomes O(L * 26^D), since there are only 2 dots so it is O(l * 26^2)==O(L)
#since all nodes stored characters upto 26 so space complexity becomes O(N*L)

#the main thing to remember is the structure of trie... each value of a dict in trie holds its own trienode, like for trie['a'] will hold the 'a' TrieNode dict



class TrieNode():
    
    def __init__(self):
        self.children={}
        self.isEnd=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()


    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.isEnd=True
        
    def search(self,word:str)->bool:

        def searchDot(node,word,depth=0):
            if not node:
                return False
            if len(word)==depth:
                return node.isEnd
            ch=word[depth]
            if ch==".":
                for child_node in node.children.values():
                    if searchDot(child_node,word,depth+1):
                        return True
            else:
                if ch not in node.children:
                    return False
                node=node.children[ch]
                return searchDot(node,word,depth+1)
            return False
        return searchDot(self.root,word,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)