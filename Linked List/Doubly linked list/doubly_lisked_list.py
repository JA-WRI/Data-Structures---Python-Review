# all nodes will contain three parts: pointer to previous node, data, pointer to next node
class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None  
        self.prev = None

class DoublyLinkedList:  
    def __init__(self):  
        #note you don't need to have a pointer to the tail but it will make inserting at the end faster
        self.head = None  
        self.tail = None 


    def append(self, data):  
        new_node = Node(data)  
        if self.head is None:  # when list is empty we signed the head and tail to same node
            self.head = new_node  
            self.tail = new_node  
        else:  
            self.tail.next = new_node  # ---> tail ---> newNode
            new_node.prev = self.tail  
            self.tail = new_node       # ---> prev ---> tail
    
    def traverse_forward(self):  
        current = self.head  
        while current:  
            print(current.data)  
            current = current.next
    
    def traverse_backward(self):  
        current = self.tail  
        while current:  
            print(current.data)  
            current = current.prev
   
    def insert_at_beginning(self, data):  
        new_node = Node(data)  
        if self.head is None:  
            self.head = new_node  
            self.tail = new_node  
        else:  
            new_node.next = self.head  
            self.head.prev = new_node  
            self.head = new_node


    def insert_at_position(self, data, position):  
        if position <= 0:  
            return  
        new_node = Node(data)  
        current = self.head  
        for _ in range(position - 1):  
            if current is None:  
                return  
            current = current.next  
        if current is None:  
            return  
        new_node.next = current.next 
        new_node.prev = current  
        if current.next:  
            current.next.prev = new_node  
        current.next = new_node

    def delete_at_position(self, position):  
        if position <= 0 or self.head is None:  
            return  
        current = self.head  
        for _ in range(position - 1):  
            if current is None:  
                return  
        current = current.next  
        if current is None or current.next is None:  
            return  
        if current.next == self.tail:  
            self.tail = current  
            self.tail.next = None  
        else:  
            current.next = current.next.next  
            if current.next:  
                current.next.prev = current