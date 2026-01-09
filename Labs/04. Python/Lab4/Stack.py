class Stack:
    def __init__(self,size):
        self.size=size
        self.items=[]
        self.tos=-1

    def is_empty(self):
        return self.tos==-1

    def push(self,item):
        if self.tos==self.size-1:
            print("Stack Overflow!")
        else:
            self.tos+=1
            self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is Empty!")
        else:
            self.tos-=1
            return self.items.pop()

    def display_stack(self):
        return self.items

    def search(self,item):
        for i in range(len(self.items)):
            if item==self.items[i]:
                return i
        return -1



s=Stack(3)
s.push(5)
s.push(7)
s.push(8)
print(s.display_stack())

print(s.search(8))

