class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() <= 0:
            return None
        val = self.stack[self.size()-1]
        self.stack.pop()
        return val

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() <= 0:
            return None
        return self.stack[self.size()-1]
        
def check_balanced(str):
    st = Stack()
    for i in range(0, len(str)):
        c = str[i]
        if c == '(':
            st.push(i)
        else:
            if st.size() == 0:
                return False
            st.pop()
    return st.size() == 0

