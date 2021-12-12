class Stack:
    def _init_(self):
        self.items = []
        self.size = 0
        
def push(self, data):
    self.items.append(data)
    
def pop(self):
    return self.items.pop()

def size(self):
    return self.size

def is_Empty(self):
    return self.items == 0

def peek(self):
    if not self.is_empty():
        return self.items[-1]

push("e")
pop()
is_Empty()
peek()

class Queue:
    def _init_(self):
        self.items = []
        self.size = 0

def enqueue(self, data):
    self.items.insert(0, data)
    self.size += 1
    
def dequeue(self):
    data = self.items.pop()
    self.size -= 1
    return data

def size(self):
    return self.size

def is_Empty(self):
    return self.items == 0

def peek(self):
    if not self.is_empty():
        return self.items[-1]

enqueue("e")
Queue.size()
Queue.dequeue()
Queue.is_Empty()
Queue.peek()