class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        vals = []
        current = self.head
        while current is not None:
            vals.append(str(current.value))
            current = current.next
        return " <-> ".join(vals)
    
    def append(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
    def prepand(self, value):
        new_node = DoublyNode(value)        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def remove(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False