from stack import Stack

st = Stack()
assert st.isEmpty() == True

# Push elements onto the stack
st.push(1)
st.push(2)
st.push(3)
st.push(4)

# test isEmpty
assert st.isEmpty() != True

# test peek and pop
assert st.peek() == 4
assert st.pop() == 4
assert st.pop() == 3
assert st.pop() == 2
assert st.peek() == 1
assert st.pop() == 1
assert st.peek() == None
assert st.pop() == None

assert st.isEmpty() == True

print("All test pass")

