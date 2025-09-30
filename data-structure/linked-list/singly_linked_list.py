class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        vals = []
        current = self.head
        while current is not None:
            vals.append(str(current.value))
            current = current.next
        return " -> ".join(vals)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev
        
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        
    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def remove(self, value):
        current = self.head
        prev = None
        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False
        
if __name__ == "__main__":
    lst = LinkedList()
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
    
    lst.reverse()
    print(lst)