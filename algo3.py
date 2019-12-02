# Algo 3
# Stack

data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack.pop())

# Stack 구현하기

class MyStack:
    def __init__(self):
        self.stack = []
    def pop(self):
        return self.stack[-1]
    def push(self, data):
        self.stack.append(data)
data_stack = MyStack()

data_stack.push(1)
data_stack.push(2)

print(data_stack.pop())
