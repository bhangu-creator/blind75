#creating a stack class for fixed array length to undertstnad the stack better. 
#first we created a constructor, its job is to basically provides attributes to the object. It uses self as to tell python that which instance of object to refer to
#then we just created different stack methods and used them accordingly
#main point is just constructor and how to initialze the attributes of object


class Stack :
    
    #creating the constructor for stack class to intialize attributes of stack class's object
    def __init__(self,cap):
        self.cap=cap
        self.top= -1
        self.stk=[0]*cap
        
    #push is used to push elements in the stack
    def push(self,elem):
        if self.top>=self.cap-1:
            print(" Stack Overflow message in push")
            return False
        else :
            self.top=self.top+1
            self.stk[self.top]=elem
            return True
        
    #pop is used to pop the elements from the stack
    def pop(self):
        if self.top==-1:
            print("Stack is empty message in pop")
            return 0
        else:
            ret= self.stk[self.top]
            self.top=self.top-1
            return ret
        
    #peek is used to check the top most element of the stack
    def peek(self):
        if self.top==-1:
            print("Stack is empty message in peek")
            return 0
        else:
            return self.stk[self.top]
    
    #isEmpty is used to check if Stack is empty or not
    def isEmpty(self):
        if self.top==-1:
            print("Stack is empty message in isEmpty")
            return True
        else:
            return False
        
    #isFull is used to check if the stack is full or not
    def isFull(self):
         if self.top>=self.cap-1:
            print(" Stack Overflow message in isFull")
            return True
         else:
            return False
     
#creating object of Stack class       
s= Stack(5)

#testing the created methods
s.push(5)
s.push(8)
s.push(2)
s.push(10)
print(s.isFull())
s.push(80)
print(s.isFull())
s.pop()
print(s.isEmpty())
s.pop()
s.pop()
s.pop()
s.pop()
print(s.isEmpty())

              
        
