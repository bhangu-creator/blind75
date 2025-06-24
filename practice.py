from typing import List
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs={}
        freqt={}
        left=0
        required=len(t)
        formed=start=end=0
        minlength=float('inf')
        for i in range(len(t)):
            if t[i] not in freqt:
                freqt[t[i]]=1
            else:
                freqt[t[i]]+=1
        for right in range(len(s)):
            if s[right] not in freqs:
                freqs[s[right]]=1
            else:
                freqs[s[right]]+=1
            if s[right] in freqt and freqs[s[right]]==freqt[s[right]]:
                formed+=1
            while required==formed:
                windowlength=right-left+1
                if windowlength<minlength:
                    start=left
                    end=right
                    minlength=windowlength
                if s[left] in freqt and freqs[s[left]]==freqt[s[left]]:
                    formed-=1
                freqs[s[left]]-=1
                left+=1
        return "" if minlength==float('inf') else s[start:end+1]

            


            
        

sol=Solution()
val=sol.minWindow("aa","aa")
print(val)
        
        