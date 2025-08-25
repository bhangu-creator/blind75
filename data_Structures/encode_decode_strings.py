

class Solution:

    def encode(self, strs) -> str:
        if len(strs)<1:
            return ""
        encode_string=""
        for word in strs:
            encode_string+=str(len(word))+"#"+word
        return encode_string

    def decode(self, s: str) :
        if s=="":
            return []
        word=""
        strs=[]
        indx=0
        number=""
        while indx<len(s):
            if s[indx]!="#":
                number+=s[indx]
            else:
                number=int(number)
                word+=s[indx+1:indx+number+1]
                strs.append(word)
                indx+=number
                word=""
                number=""
            indx+=1
        return strs