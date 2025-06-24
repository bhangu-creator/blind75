class Solution:
    
    #this is my orginal version
    
    def minWindow(self, s: str, t: str) -> str:
        freqt={}
        freqw={}
        startIdx=lastIdx=float('-inf')
        restr=""
        minwin=float('inf')
        for i in range(len(t)):
            if t[i] not in freqt:
                freqt[t[i]]=1
            else:
                freqt[t[i]]+=1
        j=0
        for i in range(len(s)):
            windowLength=i-j+1
            if s[i] not in freqw:
                    freqw[s[i]]=1
            else:
                freqw[s[i]]+=1
                        
            while all(freqw.get(k, 0) >= v for k, v in freqt.items()): #memorize this 
                if windowLength<minwin:
                    minwin=windowLength
                    startIdx=j
                    lastIdx=i
                freqw[s[j]]-=1
                j+=1
                windowLength=i-j+1
    
        if  startIdx>=0 and lastIdx>=0:
            for k in range(startIdx,lastIdx+1):
                restr+=s[k]
        return restr
            
            
        #following is the more readable and efficent version using AI, this version is O(m+n) time complexity 
        
        
        

#this is a sliding window problem, the window is valid when all the characters from t string are present inside the window
#we have used freq counter to validate the window, when window gets valid we will start removing characters from left by incrementing left and reducing its frequency by 1 till when window becomes invalid
#when window became invalid we will then again start expanding it using right pointer to make it valid again. we will keep the min window length and with that its start and end min length which will be our right

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        # Count frequency of characters in t
        freqt = Counter(t)  # Example: t = "ABC" -> freqt = {'A': 1, 'B': 1, 'C': 1}

        freqw = {}  # To store character counts in current sliding window from s

        min_len = float('inf')  # To track the length of the minimum window
        start = 0               # To track the starting index of the best window
        left = 0                # Left pointer of the sliding window

        formed = 0              # Number of characters with required frequency in current window
        required = len(freqt)   # Number of unique characters in t to be matched

        # Expand the window with the right pointer
        for right in range(len(s)):
            char = s[right]  # Current character at right pointer

            # Update frequency of the current character in the window
            freqw[char] = freqw.get(char, 0) + 1

            # If the current character is in freqt and we reached its desired count
            if char in freqt and freqw[char] == freqt[char]:
                formed += 1  # One more required character is fully matched

            # Now try to shrink the window from the left while it's valid
            while formed == required:
                window_len = right - left + 1  # Current window size

                # If it's the smallest valid window so far, update result
                if window_len < min_len:
                    min_len = window_len
                    start = left

                # Remove the leftmost character from the window
                freqw[s[left]] -= 1

                # If it was a required character and we dropped below its required count
                if s[left] in freqt and freqw[s[left]] < freqt[s[left]]:
                    formed -= 1  # No longer fully valid

                # Move left pointer forward to reduce window size
                left += 1

        # Return the minimum window substring or empty string if no such window
        return s[start:start+min_len] if min_len != float('inf') else ""


          
        

sol=Solution()
s="abdecfab"
t="abc"
val=sol.minWindow(s,t)
print(val)
        
        