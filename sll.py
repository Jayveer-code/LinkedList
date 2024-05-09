class Node:
    def __init__(self, data):
        # Step 1: Initialize Node with data and next reference
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Step 2: Initialize LinkedList with head node as None
        self.head = None

    def is_empty(self):
        # Step 3: (Condition no 1) Check if the LinkedList is empty
        return self.head is None

    def print_list(self):
        # Step 4: (Condition no 2) Print the elements of the LinkedList
        if self.is_empty():
            print("Linked List is Empty")
        else:
            # Step 5: (Condition no 3) If it is Not None that what to do
            new_node = self.head  
            while new_node:
                print(new_node.data,end = "  --->  ")
                new_node = new_node.next

    def add_beginning(self, data):
        # Step 6: Add a new node at the beginning of the LinkedList
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        # Step 6: Add a new node at the Ending of the LinkedList
        new_node=Node(data)
        if self.head is None: #Ckeck  LL is Empty Or not
            self.head=new_node
        else:
            n=self.head
            while n.next is not None: # Increment Next Value Until Condition is True
                n=n.next 
            n.next=new_node

    def add_after(self,data,x):#x iis uuse For target element
        n=self.head
        #when n is not none then target element
        while n is not None:
            if x==n.data:
                break
            n=n.next
            #when n is  none then print msg
        if n is None:
            print("Element Not Present in LL..")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Element", x, "not found in the linked list.")
            return 
        new_node = Node(data)
        new_node.next = n.next
        n.next = new_node

    def del_begin(self):
        if self.head is None:
            print("Linked List is Empty so we can not Delete Any Nodes!. ")
        else:
            self.head=self.head.next

    def del_end(self):
        if self.head is None:
            print("Linked List is Empty so we can not Delete Any Nodes!. ")
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None

    def del_by_value(self,x):
        if self.head is None:
            print("Linked List is Empty so we can not Delete Any Nodes!. ")
            return
        if x==self.head.data:
            self.head=self.head.next
            return
        n=self.head
        while n.next is not None:
            if x==n.next.data:
                break
            n=n.next
        if n.next is None:
            print("Element", x, "not found in the linked list.")
        else:
            n.next=n.next.next

            
        





LL1 = LinkedList()
LL1.add_beginning(11)
LL1.add_end(14)
LL1.add_after(12,11)
LL1.add_after(13,12)
LL1.add_before(10,11)
LL1.del_by_value(13)
# LL1.del_begin()
# LL1.del_end()

LL1.print_list()
