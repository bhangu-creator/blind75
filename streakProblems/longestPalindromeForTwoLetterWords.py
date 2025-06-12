#count the frequency of each words using counter
#for the words which don't have same letters but reverse exist we can simply pair them with thier reverse with the minimum freq as that is the only possible pair number
#for the words which has same letters and reverse exist we can just use even no and if there is odd left we only need to use 1 

from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        res=0
        isOdd=False
        for word,count in counter.items():
            rev= word[::-1]
            if rev==word:
                if count%2==0:
                    res=res+count
                else:
                    res=res+ count-1
                    isOdd=True
            elif word<rev:
                res=res+min(count,counter[rev])*2
        if isOdd==True:
            res=res+1
        return res*2
    
Sol=Solution()
val=Sol.longestPalindrome(["lc","cl","gg"])
print(val)
