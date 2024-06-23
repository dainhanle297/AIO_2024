class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Or raise an exception for empty stack

    def push(self, value):
        if not self.is_full():
            self.items.append(value)
        else:
            pass  # Or raise an exception for full stack

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Or raise an exception for empty stack


stack1 = Stack(capacity=5)

stack1.push(1)

stack1.push(2)

print(stack1.is_full())

print(stack1.top())

print(stack1.pop())

print(stack1.top())

print(stack1.pop())

print(stack1.is_empty())
