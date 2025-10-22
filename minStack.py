class MinStack:

    def __init__(self):
        self.rootStack=[]

    def push(self, val: int) -> None:
        stack=self.rootStack
        if not stack:
            stack.append((val,val))
        else:
            minval=min(stack[-1][1],val)
            stack.append((val,minval))
        
    def pop(self) -> None:
        stack=self.rootStack
        stack.pop()
        

    def top(self) -> int:
        stack=self.rootStack
        return stack[-1][0]
        

    def getMin(self) -> int:
        stack=self.rootStack
        return stack[-1][1]

#the problem was in this problem to get the minimum element of stack in O(1) time, we can do this by storing the min element with each value that can tell us that what 
#is the minimum value in the stack in constant time

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()