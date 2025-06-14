

class Solution:
    def minMaxDifference(self, num: int) -> int:
        smax=str(num)
        smin=str(num)
        remap=smax[0]
        remin=smin[0]

        for i in range(len(smax)):
            if smax[i]!='9':
                remap=smax[i]
        smax =smax.replace(remap, '9')
        smin=smin.replace(remin,'0')

        return int(smax)-int(smin)
        

sol=Solution()
val=sol.minMaxDifference(9566477)
print(val)
        
        