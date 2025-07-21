class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        retArr=[s[0]]
        cnt=1
        for indx in range(1,len(s)):
            if s[indx]==retArr[-1]:
                cnt+=1
                if cnt<3:
                    retArr.append(s[indx])
            else:
                cnt=1
                retArr.append(s[indx])
        return "".join(retArr)