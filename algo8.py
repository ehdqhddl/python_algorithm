# Algo8
# 힙 자료구조 기초 및 실습


class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)

        insert_idx = len(self.heap_array) - 1

        while self.heap_array[insert_idx] > self.heap_array[insert_idx//2] and insert_idx != 1:
            temp_value = self.heap_array[insert_idx//2]
            self.heap_array[insert_idx//2] = self.heap_array[insert_idx]
            self.heap_array[insert_idx] = temp_value
            insert_idx = insert_idx//2

        return True


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
print(heap.heap_array)
heap.insert(11)
heap.insert(12)
heap.insert(6)
print(heap.heap_array)


