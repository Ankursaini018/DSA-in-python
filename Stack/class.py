class stack:

    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.item.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.item[-1]

    def is_empty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def display(self):
        print("stack (top>bottom):", self.item[::-1])

S = stack()
S.push(1)
S.push(2)
S.push(3)
print("after pushing 1,2,3")
S.display()

print("top item", S.peek())
print("popped item", S.pop())
print("after popping")
S.display()
print("total size", S.size())        
print("is stack empty?", S.is_empty())