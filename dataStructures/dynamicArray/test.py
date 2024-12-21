from dynamicArray import DynamicArray

x = DynamicArray()

# test popping empty 
x.pop()
assert str(x) == "[]"
assert x.size == 0
assert x.capacity == 5

x.append(1)
x.append(2)
x.append(3)
assert str(x) == "[1 2 3]"
assert x.size == 3
assert x.capacity == 5

x.insert(0,0)
x.insert(0, 3)
x.insert(0, 5) 
x.insert(4, 50)
assert str(x) == "[0 1 2 0 3 0 4]"
assert x.size == 7
assert x.capacity == 10

x.append(5)
x.append(6)
x.append(7)
x.append(8)
assert str(x) == "[0 1 2 0 3 0 4 5 6 7 8]"
assert x.size == 11
assert x.capacity == 20

x.pop(0) # first 0
x.pop(2) # second 0, index has now moved down 1 from insert at 3
x.pop(3) # third 0 index has now moved down 2 from insert at 5
x.pop()
x.pop(100)
assert str(x) == "[1 2 3 4 5 6]"
assert x.size == 6
assert x.capacity == 10

print("All tests passed")