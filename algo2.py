# Algo 2
# Queue

# Queue 클래스 만들기

class myQueue:
    def __init__(self):
        self.queue = []
    def deque(self):
        self.queue.pop(0)
    def enque(self,data):
        self.queue.append(data)
    def getHead(self):
        return self.queue[0]
    def getTail(self):
        return self.queue[-1]
    def printList(self):
        return self.queue

que = myQueue()

que.enque(10)
que.enque(11)
que.enque(12)
que.enque(14)

print(que.printList())
que.deque()
print(que.printList())

print("----------------------------")
print("----------------------------")

# Queue 클래스 사용하기

import queue

data_queue = queue.Queue() # FIFO 일반적인 큐

data_queue.put(1)
data_queue.put(2)

# print(data_queue.qsize())
print(data_queue.get())

print("----------------------------")
print("----------------------------")

data_queue = queue.LifoQueue() # LIFO 큐

data_queue.put(1)
data_queue.put(2)

print(data_queue.get())

data_queue = queue.PriorityQueue() # Priority 큐

data_queue.put((10, "b")) # 첫번쨰항목이 우선순위, 두번쨰가 항목 / 우선순위 값이 낮을수록 높음
data_queue.put((5, "a"))
data_queue.put((17, "z"))

print(data_queue.get())

