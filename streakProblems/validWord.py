class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowel={'a':True,'e':True,'i':True,'o':True,'u':True}
        isvowel=False
        isconsonant=False
        for i in range(len(word)):
            if word[i].isalpha():
                char=word[i].lower()
                if char in vowel:
                    isvowel=True
                else:
                    isconsonant=True
            elif not word[i].isdigit():
                return False
        if isconsonant and isvowel:
            return True
        else:
            return False

        
        
        