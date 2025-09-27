# each node will contain two parts: one for data and one that points to the next node
class Node:  
    def __init__(self, data=None):  
        self.data = data  
        self.next = None

class LinkedList:  
    # every linked list has a head that points to the first node
    def __init__(self):  
        self.head = None  

    # This is a traverse method that starts from the head node 
    # and iterates through each node using the next reference
    def traverse(self):  
        current = self.head  
        while current:  
            print(current.data, end=" -> ")  
            current = current.next  
            print("NULL")
    

    # creates a new node and updates its next reference to point 
    # to the current head of the list. The head is then updated to the new node
    def insert_at_beginning(self, data):  
        new_node = Node(data)  
        new_node.next = self.head  
        self.head = new_node

    # method traverses the list to find the last node and updates the 
    # next reference of the last node to point to the new node.
    def insert_at_end(self, data):  
        new_node = Node(data) 

        if not self.head:  
            self.head = new_node  # if linked list is empty we make the current data the head 
            return  
        last = self.head  # we need to iterate through the whole linked list in order to append to the end
        while last.next:  
            last = last.next  
            last.next = new_node 

    def insert_at_position(self, data, position):  
        new_node = Node(data)  

        if position == 0:  
            new_node.next = self.head  
            self.head = new_node  
            return  
        
        current = self.head  
        for _ in range(position - 1):  
            current = current.next  
            if not current:  
                raise IndexError("Position out of bounds")  
        new_node.next = current.next  
        current.next = new_node


    def delete_node(self, key):  
        temp = self.head  
        if temp is not None:  
            if temp.data == key:  # if we want to get ride of the first node
                self.head = temp.next  # asiging the next node as the head 
                temp = None 
                return 
        while temp is not None:  
            if temp.data == key:  
                break 
            prev = temp  
            temp = temp.next
        if temp == None:  
            return
        prev.next = temp.next  # --> prev ---> temp ---> temp.next
                               # --> prev.next ---> temp.next
        temp = None

        def search(self, key):  
            current = self.head  
            while current:  
                if current.data == key:  
                    return True 
                current = current.next 
            return False
        


