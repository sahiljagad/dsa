class DynamicArray():
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.array = [None] * self.capacity
    
    def __repr__(self):
        return self.__str__()
  
    def __str__(self):
        return "[" + " ".join([str(x) for x in self.array if x != None]) + "]"
    
    def _grow(self):
        self.capacity *= 2
        self.array += [None] * (self.capacity - self.size)

    def _shrink(self):
        self.capacity //= 2

    def append(self, val):
        #check if we have reached cappacity and grow accordingly
        if self.size == self.capacity:
            self._grow()
        #add value to end
        self.array[self.size] = val
        self.size += 1
    
    def pop(self, index=-1):
        # cannot pop from empty list
        if self.size == 0:
            return
        
        # if no index is passed in, set index to last element
        if index == -1 or index >= self.size: 
            index = self.size - 1

        # shift every element after index to left
        for i in range(index, self.size):
            if i == self.size - 1:
                self.array[i] = None
                break
            self.array[i] = self.array[i + 1]

        # decrease size by 1
        self.size -=1

        # decrease capacity if about half the elements are gone 
        # +1 on self.size bc we can divide by 0
        if (self.capacity // (self.size + 1)) > 1:
            self._shrink()
        
    def insert(self, val, index):
        # check if element at end or not in range of indices to be added to
        if index >= self.size:
            self.append(val)
            return
            
        #check if we have reached cappacity and grow accordingly
        if self.size == self.capacity:
            self._grow()

        # shift all elements from index to right
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        
        # add value at index
        self.array[index] = val

        # increase size by 1
        self.size +=1

