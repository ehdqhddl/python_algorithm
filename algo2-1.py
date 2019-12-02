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
inVal = []
que = MyQueue()
for i in range(int(N)):
    inVal = sys.stdin.readline().split()
    if inVal.find('push') != -1:
        que.push(inVal.split(sep=' ')[1])
    elif inVal.find('pop') != -1:
        que.pop()
    elif inVal.find('front') != -1:
        que.front()
    elif inVal.find('back') != -1:
        que.back()
    elif inVal.find('size') != -1:
        que.size()
    else:
        que.empty()