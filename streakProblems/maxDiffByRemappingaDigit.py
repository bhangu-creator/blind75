class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        for ch in s:
            if ch !='9':
                smax=s.replace(ch,'9')
                break
        else:
            smax=s
        smin =s.replace(s[0], '0')
        return int(smax)-int(smin)
    
sol=Solution()
val=sol.minMaxDifference(90)
print(val)