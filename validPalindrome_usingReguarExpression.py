import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we can use the re module of python which is a regular expression module to get rid of all non-alphanumeric characters in the string
        
        #here is the code to do exactly that
        res = re.sub(r'[^a-zA-Z0-9]',"",s)
        
        #now using another variable to convert this string alphanumeric string to lowercase
        res_lower=res.lower()     
        
        #now the string has become strict alphanumeric & lower case,now we need to check if it is a vaid palindrome
        #to do that we first will reverse the given string and assign it to a new variable like newRes
        newRes=res_lower[::-1]
        
        #now we have two strings one is res which is alphanumeric and other is newRes which is reverse of "res"
        # we acheived this by using slicing in python (read about it again)
        #now we need to compare both of these strings using comparison operater. if they are equal that will means that it is a valid palindrome
        
        if res_lower==newRes :
            return True
        else:
            return False
        
        
s =  Solution()
bol= s.isPalindrome("A man, a plan, a canal: Panama")
print(bol)