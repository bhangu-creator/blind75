class Solution:
    
    #ok so first I will say to look in your notebook solution for this then read the following
    #so first thing is by reading the problem we know it is a substring problem and we can use sliding window algo since it will scan every possible substring in the string
    #next thing is a sliding window algo usually starts with 2 pointers left and right at initial position of 0, then the algo will increment right pointer in our solution it always increment by 1 and then it will check if the elements/characters in the window/substring matches the sceanrio in simple terms is the substring/window is valid or invalid
    #if the window is invalid then we usualy reduce the window length or increse it , in our solution we decrease the window length by 1 from left side and also increment the right pointer and check the validity of window in next iteration
    #by incrementing/decrementing the window only by 1 index it ensures that the window covers all the possible valid substrings
    #now on to our problem : we had given a integrer k , this is the amount by which we can change the uppercase letters to make the substring with max length 
    #now our check of validity of window formula is  = (rightpointer-leftpointer + 1) - maxFrequency of the characters in the substring <=k
    #here (rightpointer-leftpointer + 1) this thing represents our valid window's length. we are adding +1 in this as our pointers start from 0 so by adding 1 it ensure the length is correct.
    #rightpointer will be our variable defined in our loop i.e i , as it always increment by 1 so window will always increase by 1
    #left pointer i.e j will be at 0 at Start and it will be incremented , decreasing the length of the window by 1 if our formula which is (rightpointer-leftpointer + 1) - maxFrequency of the characters in the substring is >k
    #we will also decrement the frequency of the character which is present at j pointer this will ensure that now we are not taking the count of that character into account for the next operation to check the validity of the substring
    #now to undertstand the above formula we need to understand that window length- max frequency of character will give us the count of characters which are different , so if they are >k  that would mean we cannot change them as we can only do it only k times so that is why the window becomes invalid
    #but if it is <=k that would mean that we can convert all the different characters and our all characters in the substring will become equal , then we will calculate the length of the substring , In the END the maximum substring length that we stored wil be our solution
    
    
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}   #initialzing hashmap to store frequencies of all characters
        j=0       #initialzing the left pointer
        maxfreq=maxlength=float('-inf')     #initializing the maxfreq and maxlength variables
        for i in range(0,len(s)):  #i in the loop is going to be our right pointer
            if s[i] not in freq:   #right pointer will increment by 1 
                freq[s[i]]=1       #will store the frequency of the character present at i , right pointer
            else: 
                freq[s[i]]+=1      #will increment the frequecny of the character
            maxfreq=max(maxfreq,freq[s[i]])    #will calculate the mafreq of the character in the substring 
            if (i-j+1)-maxfreq>k:      #will check the validity of the window 
                freq[s[j]]-=1          #will decrement the frequency of the character at i pointer making sure it is not getting into account for next window validity
                j+=1                   #will increment the left pointer cutting out the left character out of window
            else:
                maxlength=max(maxlength,(i-j+1))   #if the window is valid then the maxlength of valid substring will be stored here
        return maxlength       #when loop ends the max length of substring that was present in the string will be returned

sol=Solution()
val=sol.characterReplacement("AABABBA",1)
print(val)



                

        
        