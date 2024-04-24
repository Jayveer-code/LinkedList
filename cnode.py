
# Step 1 Create Node 
class Node:
    def __init__(self,data):
        self.data =data
        self.ref =None
#Step 2 Creatre indivisual Node using Node Class  Make Another Class LinkedList for link Node 
class LinkedList:
    def __init__(self):
        self.head=None
#Step 3 Now Travese the List 
#Condition 1 LL is empty
    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty :::")
#Condition 2 LL is not empty
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
#Insert data In the beigning
    def add_begin(self,data):
        new_node =Node(data)
        new_node.ref=self.head
        self.head=new_node



LL1=LinkedList()
LL1.add_begin(30)
LL1.add_begin(20)
LL1.add_begin(10)
LL1.print_LL()
#  it gives the refrence number for connect other link niche wada
# Node1 = Node(10)
# print(Node1)
        
