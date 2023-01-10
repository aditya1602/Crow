class Stack:
    def __init__(self, items = []):
        self.items = items
    
    def pushItem(self, item):
        self.items.append(item)
    
    def popItem(self):
        if (self.items):
            return self.items.pop()
        else:
            print("Stack is empty!!")
    
    def countItems(self):
        return self.items.count()
    
    def displayAll(self):
        for item in self.items:
            print(item)

stack = Stack()