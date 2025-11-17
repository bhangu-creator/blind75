from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq1=Counter(s1)
        freq2={}
        leng=len(s1)
        left=0
        for right in range(len(s2)):
            if s2[right] not in freq2:
                freq2[s2[right]]=1
            else:
                freq2[s2[right]]+=1

            if (right-left)+1>leng:
                freq2[s2[left]]-=1
                if freq2[s2[left]]<=0:
                    del freq2[s2[left]]
                left+=1
            if (right-left)+1==leng and freq2==freq1:
                return True
        return False
    
# the main intuation is we can say a string s1 is permutation of s2 if freq(s1)==freq(s2) , after this its just standard anagram code using sliding window
#time is O(n) and space is O(n)
            


