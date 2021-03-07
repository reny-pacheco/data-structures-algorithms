

class LinkedList:
    def __init__(self, nodes= None):
       self.head = None
       if nodes is not None:
           node = Node(data=nodes.pop(0))
           self.head = node

           for elem in nodes: 
               node.next = Node(data=elem)
               node = node.next

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        nodes.append("None")
        return " -> " .join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    def get_node(self, i):
        if self.head is None:
            raise Exception("List is empty")
        
        for count, node in enumerate(self, start = 1):
            if i == node.data:
                print(count)
        print('not found')

    def reverse(self):
        if self.head is None:
            raise Exception("List is empty")
        
        previous_node = None
        current_node = self.head

        while current_node.next:
            tmp = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = tmp
        
        current_node.next = previous_node
        self.head = current_node

           
        

            
        
        
        


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        node = self.data


llist = LinkedList(["a", "b", "c", "d"])

print(llist)
llist.reverse()
print(llist)








        