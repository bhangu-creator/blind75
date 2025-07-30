from typing import Tuple

class Solution:
    #we use stack in this problem and it is done as we need to preserve order of substrings
    #the intuation is simple , we use greedy to add the gains of the most optimal sub string and pushed the rest of the strings in the stack
    #when all the chars are processed or we get a char which is not a or b then we simply just process all the chars in stack till its empty and the gains in totalgain
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def emptyStack(stack):
            a_cnt=b_cnt=temp_gain=0
            while stack:
                ch=stack.pop()
                if ch=='a':
                    a_cnt+=1
                else:
                    b_cnt+=1
            temp_gain+=min(a_cnt,b_cnt)*min(x,y)
            return temp_gain
        totalGain=0
        stack=[]
        for ch in s:
            if ch=='a' and stack and stack[-1]=='b':
                if y>x:
                    stack.pop()
                    totalGain+=y
                else:
                    stack.append(ch)
            elif ch=='b' and stack and stack[-1]=='a':
                if x>y:
                    stack.pop()
                    totalGain+=x
                else:
                    stack.append(ch)
            elif ch!='a' and ch!='b':
                totalGain+=emptyStack(stack)
            else:
                stack.append(ch)
        if stack:
            totalGain+=emptyStack(stack)
        return totalGain 


    #this is the minimist version of above code , it does thesame thing but instead of using nested if and elsewe just use a helper method to process all the stack operations
    #the important part is we have to process the substrings with max value... because x+y is always greater than y+y if x>y
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s: str, first: str, second: str, value: int) ->Tuple[str,int]:
            stack=[]
            gain=0
            for ch in s:
                if stack and ch==second and stack[-1]==first:
                    stack.pop()
                    gain+=value
                else:
                    stack.append(ch)
            return "".join(stack),gain
        if x>y:
            s,gain1=remove_substring(s,'a','b',x)
            _,gain2=remove_substring(s,'b','a',y)
        else:
            s,gain1=remove_substring(s,'b','a',y)
            _,gain2=remove_substring(s,'a','b',x)
        return gain1+gain2
    
    #same prooblem but using no stack :

    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removeStrings(s,first,second,value):
            s=list(s)
            read=write=0
            n=len(s)
            gain=0
            while read<n:
                if write>0 and s[write-1]==first and s[read]==second:
                        write-=1
                        gain+=value
                else:
                    s[write]=s[read]
                    write+=1
                read+=1
            s="".join(s)
            return s[:write],gain
        if x>y:
            s,gain1=removeStrings(s,'a','b',x)
            _,gain2=removeStrings(s,'b','a',y)
        else:
            s,gain1=removeStrings(s,'b','a',y)
            _,gain2=removeStrings(s,'a','b',x)
        return gain1+gain2








