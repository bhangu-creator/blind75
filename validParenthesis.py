
# This problem can be used using Stack data structure. We will push all the characters in the stack untill we got a character
# which includes a closing parenthesis character, the we will pop the top most element as it is sure to be the last opening parenthesis
# i first wrote the code by using many if else condition but I have found out that we can clean the code very much using 
# dictionaries so here is that code

class Solution:
    def isValid(self, s: str) -> bool:
        
        #first create a dicionary in which we will put the close parenthesis as keys since we just need to focus on those because when we encounter a close parenthesis we need to pop its corresponding open parenthesis
        # we also mapped the corresponding open parenthesis with the closed one
        parenth_dict={'}':'{',')':'(',']':'['}
        
        # now initialze an array which will act as our stack
        stak = []
        
        #loop through the string
        for charc in s:
            if charc in parenth_dict:
                
                #checking if stack is not empty and also if the top most element of stack is a open parenthesis
                if stak and stak[-1]==parenth_dict[charc]:
                    
                #when both the conditions met we will pop the top most element from stack    
                    stak.pop()
                
                #if the top most element is not a open parenthesis that would mean that the string is invalid since a close parenthesis must have a corresponding open parenthesis, so just return false
                else:
                    return False
            else:
                #if the character is open parenthesis than just push it in our stack
                stak.append(charc)
                
         #return True as the stack is now empty     
        return not stak
                    
            
            
sol =Solution()
s="[]"
bol = sol.isValid(s)
print(bol)