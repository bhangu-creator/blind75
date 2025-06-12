class Solution:
    
    #so as mentioned in problem it is a max substring problem which means we can use the sliding window algo here
    #the window will be valid when there will be no duplicate characters inside the window/substring
    #if window is invalid at any check i.e there are duplicate characters inside the window /substring that we will keep on shrinking our window size by incrementing our left pointer and will also keep on deleting the left side characters from the substring and will check after every charcter deletion if there are duplicates or not
    #when the window/substring is free of duplicates we will add the character for which we were checking the validity of window and so on
    #till the window is valid we will check the max length and will return it in the end
    
    #pr-tip: lets say the s[right] is a character that when entered your substring made the substring invalid, so that means that there is duplicate of s[right] in the substring so to get rid of that duplicate we start to cut characters from left side as if the duplicates is in left that substring will be invalid anyways. so we needed to get rid of duplicates of s[right] in the substring
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqfreq={}
        left=0
        maxlength=0
        for right in range(len(s)):
            while s[right] in uniqfreq:
                del uniqfreq[s[left]]
                left+=1
            uniqfreq[s[right]]=1
            maxlength=max(maxlength,right-left+1)
        return maxlength

sol=Solution()
val=sol.lengthOfLongestSubstring("abcabcbb")
print(val)