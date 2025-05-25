#my approach is first converting the two strings into dictionaries , each dictionary will have the unique characters as key and the frequency of those characters will be stored in the values respectively
#then just compare both the dictionaries to get a boolean output

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict ={}; tdict={}
        
        #converting string s into the dictionary
        for charc in s:
            if charc not in sdict:
                sdict[charc]=1
            else :
                sdict[charc]= sdict[charc]+1
                
        #converting string t into the dictionary
        for charc in t:
            if charc not in tdict:
                tdict[charc]=1
            else :
                tdict[charc]= tdict[charc]+1
        
        #now comparing the both created dictionaries
        if sdict==tdict:
            return True
        else:
            return False
                

bol = Solution()
outt= bol.isAnagram("anagram","nagaram")
print(outt)