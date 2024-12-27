from abc import ABC, abstractmethod

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList(ABC):
    def __init__(self):
        self.size = 0
        self.head = None

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        ret = ""
        temp = self.head
        while temp != None:
            ret += str(temp.value) + "->"
            temp = temp.next
        
        return ret + "None"
        
        
    @abstractmethod
    def append(self):
        pass

    @abstractmethod
    def prepend(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def replace(self, index, valueß):
        pass


    