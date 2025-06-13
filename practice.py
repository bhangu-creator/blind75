from typing import List
from collections import defaultdict

class Solution:
    def countSubstrings(self, s: str) -> int:
        memo=defaultdict(lambda: False)
        n=len(s)
        count=0
        for L in range(1,n+1):
            i=0
            while L+i-1<n:
                j=L+i-1
                if i==j:
                    memo[(i,j)]=True
                elif i+1==j:
                    if s[i]==s[j]:
                        memo[(i,j)]=True
                else:
                    if s[i]==s[j] and memo[(i+1,j-1)]:
                        memo[(i,j)]=True
                if memo[(i,j)]:
                    count+=1
                i+=1
        return count   
                 
sol=Solution()
val=sol.countSubstrings("abasscjjjjckaiioakaaajjaa")
print(val)












