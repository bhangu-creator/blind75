from typing import List
from collections import defaultdict

class Solution:
    
    #there are many ways to solve this problem , I have solved it using 3 solutions:
    
    #1 Brute force recursion using memorization:
    #in this approach we basically check every single possible substring of the string and while doing that we store the data in a dictionary where key values are stored as tuple of indices and values are True or False 
    
    #2 Using Memorization Optimally:
    #in this approach instead of checking every substring possible first like 1st approach we start by checking the palindrome for 1 length string and then we check of 2 length and then all the length the idea is as follows:
    #so if the length of substring is 1 , means i and j are same so just store the value in dict as (i,i)= True
    #if the length of substring is 2 means i+1==j and also s[i] and s[j] are equal than store the value in dict as (i,j)=True
    #now for length large than > 2 we check if the outer most characters are same and also if characters on i+1 and j-1 are also same, if they are same like for length 3 we will check if s[0]==s[2] and memo[(1,1)]: if this condition is true that would mean that string from 0,3 is Palindrome and hence storing the (i,j)= True in the dict    
    #the 3rd step will be repeated for every substring with length>2 [pro tip : this is a blueprint than can be used for another palindromic problems also]
    
    #3Using the odd and even property of the palindrome: this is the most optimal approach out of 3
    #we should know that the odd length palindrome has a element at centre and all the elemnet around it are same that is how odd length palindrome gets made e.x "aaa"
    #we should also know that even length palindrome has 2 elements at centre and all the other elements around those 2 are same hence making it a plaindrome also  e.x "aaaa"
    #so in this approach for each index we will check that index for odd and even length palindrome , we will check with that character in middle can any odd or even length palindrome be made
    #for odd length we will start it with same 1 character and for even we will check for i and i+1 character
    
    def __init__(self):
        self.memo = {}        #object memo for every instance
        self.count=0          #kind of will act as global variable

    def check(self, s, i, j):
        if (i, j) in self.memo:  #this will ensure that we wont have to compute already computed strings
            return self.memo[(i, j)]

        if i >= j:                 #if all the substrings inside the string are same this condition will become true making the whole string Palindrome
            self.memo[(i, j)] = True       #storing the value 
        elif s[i] != s[j]:      #if two characters at i and j are not same then no need to check further they are not palindrome
            self.memo[(i, j)] = False #storing the value 
        else:                                   #if two characters are same then check if the substring inside them are aslo valid palindrome
            self.memo[(i, j)] = self.check(s, i + 1, j - 1)

        return self.memo[(i, j)]

    def countSubstrings(self, s: str) -> int:
        self.memo = {}  # Reset memo before starting
        count = 0
        for i in range(len(s)):         
            for j in range(i, len(s)):
                if self.check(s, i, j):
                    count += 1
        return count   
    
    
    
    def countSubstringsUsingMemo(self, s: str) -> int:
        memo=defaultdict(lambda: False)
        n=len(s)
        count=0
        for L in range(1,n+1):        #will start from  1 length and keep on increasing till n
            i=0
            while L+i-1<n:            #here L+i-1 is my j , its is the same formula as length + i - 1 , here -1 for as our index starts from 0
                j=L+i-1
                if i==j:      #for 1 Length Palindrom
                    memo[(i,j)]=True   
                elif i+1==j:          #for 2 Length Palindrome
                    if s[i]==s[j]:
                        memo[(i,j)]=True
                else:                      #for more than 2 Length Palindrome
                    if s[i]==s[j] and memo[(i+1,j-1)]:
                        memo[(i,j)]=True
                if memo[(i,j)]:      #check if the string is a palindrome
                    count+=1
                i+=1
        return count      
    
    
    
    def checkPalindrome(self,i,j,s,n):
        while i>=0 and j<n and s[i]==s[j]:       # will keep on decreasing i and increasing j as we are expanding out of centre
            self.count+=1                  #count is a global variable
            i-=1
            j+=1
    def countSubstringsUsingOddAndEvenProperty(self, s: str) -> int:
        n=len(s)
        for i in range(0,n):
            self.checkPalindrome(i,i,s,n)    #check for odd length palidrome at each index
            self.checkPalindrome(i,i+1,s,n)  #check for even length palidrome at each index
        return self.count     
    
    
    #All the above 3 approaches have Time complexity of O(n) sqaure
    
    
                 
sol=Solution()
val=sol.countSubstringsUsingOddAndEvenProperty("sososooo")
print(val)












