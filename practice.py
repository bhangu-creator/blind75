from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        uniqdict={}
        left=length=0
        maxlen=float('-inf')
        for right in range(0,len(s)):
            if s[right] not in uniqdict:
                uniqdict[s[right]]=1
                length+=1
                maxlen=max(maxlen,length)
            else:
                while left<=right:
                    if s[right] in uniqdict:
                        del uniqdict[s[left]]
                        left+=1
                        length-=1
                    else:
                        uniqdict[s[right]]=1
                        length+=1
                        break
        return maxlen
        
                        
                 
sol=Solution()
val=sol.lengthOfLongestSubstring("pwwkew")
print(val)












