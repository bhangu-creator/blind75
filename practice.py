from collections import defaultdict
from collections import deque
from typing import Optional


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        if not word.isalnum():
            return False
        vowel={'a':True,'e':True,'i':True,'o':True,'u':True,'v':True,'A':True,'E':True,'I':True,'O':True,'U':True,'V':True}
        consonant={}
        a=97
        for _ in range(26):
            consonant[chr(a)]=True
            a+=1

        isvowel=False
        isconsonant=False
        for i in range(len(word)):
            if word[i].lower() in vowel or word[i].upper() in vowel:
                isvowel=True
            if word[i] in consonant:
                isconsonant=True
            if isvowel and isconsonant:
                return True
        return False
        

sol=Solution()
bol=sol.isValid("FFa")
print(bol)
        




