class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #printing the Linked List
    def traverse(self):
        temp = self.head

        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next

    #adding node at the end
    def add_e(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        node = self.head
        
        while(node.next):
            node = node.next
        node.next = new_node

    #adding node at the beggining
    def add_b(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #deleting a node
    def del_node(self, data):
        temp = self.head

        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        
        if temp is None:
            return
        
        prev.next = temp.next
        temp = None



llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.traverse()

llist.del_node(3)
print()
llist.traverse()

llist.add_e(56)
print()

llist.traverse()
