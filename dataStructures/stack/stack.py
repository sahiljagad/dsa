class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def push(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def pop(self):
        if self.isEmpty():
            return None

        top = self.head
        top_value = self.head.value
        self.head = self.head.next
        del top
        return top_value

    def peek(self):
        return self.head.value if self.head else None

    def isEmpty(self):
        return self.head == None
