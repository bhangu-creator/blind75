#this is the trie Data structure used to do efficent operations of strings like add, search,delete etc
#since all nodes stored characters upto 26 so space complexity becomes O(N*L)
#time complexity for addword is O(L) where L is the length of the word to be inserted , since we go through each character one by one
    


class TrieNode():
    def __init__(self):
        self.children={}
        self.isEnd=False
    
class Trie():
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.isEnd=True
    def search(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                return False
            node=node.children[ch]
        return node.isEnd
    def startsWith(self,prefix):
        node=self.root
        for  ch in prefix:
            if ch not in node.children:
                return False
            node=node.children[ch]
        return True

    def delete(self,word):
        def _delete(node,word,depth=0):
            if not node:
                return False
            if depth==len(word):
                if not node.isEnd:
                    return False
                node.isEnd=False
                return len(node.children)==0
            char=word[depth]
            child=node.children.get(char)
            _should_delete_node=_delete(child,word,depth+1)
            if _should_delete_node:
                del node.children[char]
            return not node.isEnd and len(node.children)==0
        _delete(self.root,word,0)
