class Node:
    def __init__(self, data):
        # Step 1: Initialize Node with data and next reference
        self.data = data
        self.nref = None
        self.pref = None
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
            n = self.head  
            while n:
                print(n.data,end = "  --->  ")
                n = n.nref
    
    def print_list_reverse(self):
        print()
        # Step 4: (Condition no 4)How to Go Last Node
        if self.is_empty():
            print("Linked List is Empty")
        else:
            # Step 5: (Condition no 5) How to Get previous Node Of The List
            n = self.head  
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,end = "  <---  ")
                n = n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked List is Empty...")

    def add_begin(self,data):
        #condtion 1 Empty list Or Not
        #condition 2 no Empty list
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n

    def add_after(self, data, x):
     if self.head is None:
        print("LL is empty!")
     else:
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print("Given Node is not present in DLL")
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
             print("LL is empty!")
        else:
            n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print("Given Node is not present in DLL")
        else:
            new_node = Node(data)
            new_node.nref = n
            new_node.pref = n.pref
            if n.pref is not None:
                n.pref.nref = new_node
            else:
                self.head = new_node
            n.pref = new_node

    def del_begin(self):
        if self.head is None:
            print("Link list is empty so you can't delete any node.. ")
            return
        if self.head.nref is None:
            self.head=None
            print("Dll is empty after deleting a Node!..")
        else:
            self.head=self.head.nref
            self.head.pref=None

    def delete_end(self):
        if self.head is None:
            print("Link list is empty so you can't delete any node.. ")
            return
        if self.head.nref is None:
            self.head=None
            print("Dll is empty after deleting a Node!..")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None




dll=LinkedList()
dll.insert_empty(20)
dll.add_begin(5)
dll.add_end(30)
dll.add_end(60)
dll.add_after(40,30)
dll.add_before(10,20)
dll.del_begin()
dll.delete_end()
dll.print_list()
print("Forward ===>> Travesal List")
dll.print_list_reverse()
print("Backward <=== Travesal List")

