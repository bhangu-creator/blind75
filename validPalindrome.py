

# in this problem we are using two pointer approach, basic idea is just declare two pointers one at left and other at right end of the string indices
#and then compare the alphanumeric characters in lower case only and ignore the non alphanumeric characters 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #declaring the 2 pointers
        left=0
        right=len(s)-1
        
        #using while loop to access all the characters of the string
        while left<right:
            #verify if the character at left end is alphanumeric or not
            while left<right and not s[left].isalnum():
                left=left+1
            #verify if the character at right end is alphanumeric or not
            while left<right and  not s[right].isalnum():
                right=right-1
            #verify if the characters are same at both left end and right end 
            if s[left].lower()==s[right].lower():
                #incrementing and decrementing the pointers accordingly
                left=left+1
                right=right-1
            #verify if the characters are not same at both left and right end and return false if that is the case
            else:
                return False
        # return true if all the characters are same
        return True
                
s =  Solution()
bol= s.isPalindrome("A man, a plan, a canal: Panama")
print(bol)