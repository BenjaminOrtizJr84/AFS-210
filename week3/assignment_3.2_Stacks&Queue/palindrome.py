class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_Empty(self):
        return self.items == []

    def peek(self):
        if not self.is_Empty():
            return self.items[-1]

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)
             
    def dequeue(self):
        data = self.items.pop()
        return data

    def size(self):
        return len(self.items)
    
    def is_Empty(self):
        return self.items == []

    def peek(self):
        if not self.is_Empty():
            return self.items[-1]
        
newStack = Stack()
        
newStack.push("r")
newStack.push("a")
newStack.push("c")
newStack.push("e")
newStack.push("c")
newStack.push("a")
newStack.push("r")
print(newStack.pop())
print(newStack.is_Empty())
print(newStack.peek())

newQueue = Queue()

newQueue.enqueue("m")
newQueue.enqueue("a")
newQueue.enqueue("d")
newQueue.enqueue("a")
newQueue.enqueue("m")
newQueue.dequeue()
newQueue.size()
print(newQueue.dequeue())
print(newQueue.is_Empty())
print(newQueue.peek())