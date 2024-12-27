from linkedList import LinkedList, Node

class SinglyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(value)
        self.size += 1

    def prepend(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def insert(self, index, value):
        if index > self.size:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_next = temp.next
            new_node = Node(value)
            temp.next = new_node
            new_node.next = new_next
            self.size += 1

    def pop(self):
        if self.head == None:
            return
        elif self.head.next == None:
            old = self.head
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            old = temp
            temp.next = None
        del old
        self.size -= 1

    def remove(self, index):
        if self.size == 0 or index >= self.size: return
        elif index == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        elif index == self.size - 1:
            self.pop()
            return
        else:
            prev = None
            temp = self.head
            for _ in range(index):
                prev = temp
                temp = temp.next 
            prev.next = temp.next
            del temp
        self.size -= 1
            
    def get(self, index):
        if index > self.size - 1: return
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def replace(self, index, value):
        if index > self.size - 1: return
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        
