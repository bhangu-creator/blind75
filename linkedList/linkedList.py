

# Create a Node class to create a node
class Node:
    
    #this is a constructor method which will give attributes to the objects of the class Node
    def __init__(self,data):
        self.data=data
        self.next=None
        
# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
            
    #this is a method which is used to insert the node at begining of the link list   
    def insertAtBegin(self,data):    #it takes only data as input as we already know the index=0
        new_Node=Node(data)          #creates a new node
        if self.head is None:        #checks if the linked list is empty
            self.head=new_Node        #if list is empty then assigns the head to the created node
            return
        else:
            new_Node.next=self.head    #if list is not empty then assigns the head of first node of list to the new created node
            self.head=new_Node          #and make the new node the new head of the list
            
    #this method is used to insert a node at any given index of linked list     
    def insertAtAnyIndex(self,data,index):   #it takes the data and index as arguments
        if index==0:                         #checks if the index ==0 means the node is needed to be inserted at the begining so calls the method for that purpose
            self.insertAtBegin(data)
            return
        
        position=0                      #initilaze the position/index for loop to start
        current_node=self.head          #creates a temp node to use in the loop to iterate through the list
        
        while(current_node!=None and position+1!=index):   #do a while loop to check if the node at each index is empty or not and check if the next node's index is equal to the index or not
            
            position=position+1             #increment position
            current_node=current_node.next   #assigns the temp node to next node in list
            
         #loop will end when either the index is out of range means the current node is not exist Or it will end if we find the index in the list 
            
        if current_node!=None:       #here the current node is the node which is 1 index behind where we need to insert the actual node this is because when we assign the next of current node to the new node then the new node will take its place and the index will increase by 1 inserting the node at right position
            newNode=Node(data)          #new node is created
            newNode.next=current_node.next       #new node next is assigned to current node next
            current_node.next=newNode              #current node next is assigned to newnode
        else:
            print("Index out of Range")       #if the currrent node was empty then this message will get printed
          
    #this method is used when inserting a node at last of list        
    def insertAtEnd(self,data):  
        new_node=Node(data)   
        if self.head is None: #checks if the list is empty
            self.head=new_node   #if list is empty then just assign the head to new node and return
            return
        current_node=self.head      #if it is not empty then create a temp node current_node and assign the head to it
        while (current_node.next):        #traverse the whole list until current_node.next==None, loop will end when we get the last node of list
            current_node=current_node.next #keep on assigning the next of next node to current node to traverse the loop
        current_node.next=new_node    #we will get the last node here so just simply assign the next of last node to the new node
    
    #this method is used to update the link list at any index with data as value
    def updateNode(self,index,val):
        
        current_node=self.head   #creates a temp node
        position=0
        if position==index:     
            current_node.data=val
            return
        while current_node!=None and position!=index:
            current_node=current_node.next
            position+=1
        if current_node!=None:
            current_node.data=val      #update the data of the node whose index is given with data val
        else:
            print("index not present")
            
     #this method is used to delete the first node of the link list       
    def removeFirstNode(self):
        if self.head is None:           
            return
        self.head=self.head.next    #basically self.head represents the first node, so here we assigned self.head to self.head.next meaning we assigned self.head to 2nd node of linklist which makes it auto first node
        
     #this method is used to remove the last node of the link list   
    def removeLastNode(self):
        if self.head is None:
            return
        current_node=self.head
        while current_node.next!=None and current_node.next.next!=None:   #this loop insures the safety meaning if list has only 1 node then it will stop and even though that node's next is None we can do that again but the 2nd condition will only break when reaching 2nd last node, so we simply assign None to that node to make it last node
            current_node=current_node.next
        current_node.next=None    
    
    #this method will remove any node from list at any index
    def removeAtAnyIndex(self,index):
        if self.head is None:
            return
        if index==0:
            self.removeFirstNode()
            return
        
        currentNode=self.head
        position=0
        while currentNode is not None and position+1!=index:    #the loop will stop at the node which is 1 step behind the node that we want to remove
            currentNode=currentNode.next
            position+=1
            
        if currentNode is not None and currentNode.next is not None:  #this will check if current node is not out of index and if current node is not last node,because imagine in list of 4 index you were trying to remove 5th index which does not exist so the 2nd condition deals with that cases
            currentNode.next=currentNode.next.next                    #the loop will assign the 1 step behind node's next to the 1 step ahead node of the node that we wanted to remove 
        else:
            print("Index does not exist")
    
    #this method is used to remove the node using data
    def removeNodeByData(self,data):
        current_node=self.head
        if current_node.data==data:
            self.removeFirstNode()
            return
        while current_node is not None and current_node.next is not None and current_node.next.data!=data :  #this loop check if the current node's next has the data we are looking for or not, this loop will only stop if we got to the invalid node or if we are at last node or we found the data
            current_node=current_node.next
            
        if current_node is not None and current_node.next is not None:
            current_node.next=current_node.next.next
        else:
            print("data does not exist")
    
    #this method will print data of each node of link list
    def printList(self):
        current_node=self.head
        while(current_node):
            print(current_node.data)
            current_node=current_node.next
    
    #this method will return the size of link list
    def getSizeOfList(self):
        size=0
        currentNode=self.head
        while(currentNode):
            size+=1
            currentNode=currentNode.next
        return size
            
            
        
            