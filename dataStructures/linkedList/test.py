from singlyLinkedList import SinglyLinkedList

x = SinglyLinkedList()
x.prepend(1)
x.append(3)
x.insert(1, 2)
x.insert(0, 0)
assert str(x) == "0->1->2->3->None"
assert x.size == 4

x.replace(0, 1)
x.replace(1, 2)
x.replace(2, 3)
x.replace(3, 4)
assert str(x) == "1->2->3->4->None"
assert x.size == 4


x.pop() 
assert str(x) == "1->2->3->None"
assert x.size == 3


x.remove(1)
assert str(x) == "1->3->None"


assert x.get(1) == 3
x.replace(1, 2)
assert x.get(1) == 2