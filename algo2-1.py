# 백준 10845 큐 구현

import sys

class MyQueue:
    def __init__(self):
        self.queue = []
    def push(self,data):
        self.queue.append(data)
    def pop(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            data = self.queue[0]
            del self.queue[0]
            print(data)
    def size(self):
        print(len(self.queue))
    def empty(self):
        if len(self.queue) == 0:
            print(1)
        else:
            print(0)
    def front(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[0])
    def back(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[-1])

N = input()
que = MyQueue()
for i in range(int(N)):
    inVal = list(sys.stdin.readline().split())

    if inVal[0] == 'push':
        que.push(inVal[1])
    elif inVal[0] == 'pop':
        que.pop()
    elif inVal[0] == 'front':
        que.front()
    elif inVal[0] == 'back':
        que.back()
    elif inVal[0] == 'size':
        que.size()
    else:
        que.empty()
