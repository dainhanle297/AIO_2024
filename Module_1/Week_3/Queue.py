class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front_idx = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = value
            self.size += 1
        else:
            pass  # Or raise an exception for full queue

    def dequeue(self):
        if not self.is_empty():
            value = self.items[self.front_idx]
            self.front_idx = (self.front_idx + 1) % self.capacity
            self.size -= 1
            return value
        else:
            return None  # Or raise an exception for empty queue

    def get_front(self):
        if not self.is_empty():
            return self.items[self.front_idx]
        else:
            return None  # Or raise an exception for empty queue


queue1 = Queue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.get_front())
print(queue1.dequeue())
print(queue1.is_empty())
