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
        
    def prepend(self, value):
        new_node = DoublyNode(value)        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
        
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

if __name__ == "__main__":
    lst = DoublyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.prepend(5)
    print(lst) 
    
    found = lst.find(10)
    print(found.value if found else "não achou")
    
    removed = lst.remove(10)
    print("removido?", removed)
    print(lst)
    
    removed = lst.remove(100)
    print("removido?", removed)
    print(lst)