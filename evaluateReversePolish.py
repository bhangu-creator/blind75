from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid = {"+", "-", "*", "/"}
        stack=[]
        for token in tokens:
            if token in valid:
                operand1=stack.pop()
                operand2=stack.pop()
                print(operand1,operand2)
                if token=="+":
                    result=operand2+operand1
                    stack.append(result)
                elif token=="-":
                    result=operand2-operand1
                    stack.append(result)
                elif token=="*":
                    result=operand2*operand1
                    stack.append(result)
                else:
                    result=operand2/operand1
                    stack.append(int(result))
            else:
                stack.append(int(token))
        return stack[-1]

#it uses stack and we only have to perform operations when char is an operator
#time and space is O(n)



                

