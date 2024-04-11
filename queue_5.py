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
        
class Queue:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()
        
    def change(self):
        while self.input.size() > 0:
            item = self.input.pop()
            self.output.push(item)

    def enqueue(self, item):
        self.input.push(item)

    def dequeue(self):
        if self.size() <= 0:
            return None
        if self.output.size() <= 0:
            self.change()
        return self.output.pop()

    def size(self):
        return self.input.size() + self.output.size()
        
    def rotate(self, N):
        if self.size() <= 0:
            return
        for i in range(N):
            item = self.dequeue()
            self.enqueue(item)

