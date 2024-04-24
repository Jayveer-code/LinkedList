class Node:
    def __init__(self, data):
        # Step 1: Initialize Node with data and next reference
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Step 1: Initialize LinkedList with head node as None
        self.head = None

    def is_empty(self):
        # Step 1: Check if the LinkedList is empty
        return self.head is None

    def print_list(self):
        # Step 3: Print the elements of the LinkedList
        if self.is_empty():
            print("Linked List is Empty")
        else:
            new_node = self.head
            while new_node:
                print(new_node.data)
                new_node = new_node.next

    def add_beginning(self, data):
        # Step 4: Add a new node at the beginning of the LinkedList
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Example usage:
LL1 = LinkedList()
LL1.add_beginning(30)
LL1.add_beginning(20)
LL1.add_beginning(10)
LL1.print_list()
