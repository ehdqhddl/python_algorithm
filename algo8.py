# Algo 8
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
            if insert_idx == 1:
                break
        return True

    def move_down(self, head_idx):
        left_idx = head_idx * 2
        right_idx = head_idx * 2 + 1

        if left_idx >= len(self.heap_array):    # 왼쪽 자식 노드가 없을 떄
            return False
        elif right_idx >= len(self.heap_array):     # 오른쪽 자식 노드만 없을 떄
            if self.heap_array[head_idx] < self.heap_array[left_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_idx] > self.heap_array[right_idx]:
                if self.heap_array[head_idx] < self.heap_array[left_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[head_idx] < self.heap_array[right_idx]:
                    return True
                else:
                    return False

    def delete(self):
        if len(self.heap_array) <= 1:
            print('Here is nothing!')
        head_idx = 1
        return_value = heap.heap_array[1]
        heap.heap_array[1] = heap.heap_array[-1]
        del heap.heap_array[-1]

        while self.move_down(head_idx):
            left_idx = head_idx * 2
            right_idx = head_idx * 2 + 1

            if right_idx >= len(self.heap_array):  # 오른쪽 자식 노드만 없을 떄
                if self.heap_array[head_idx] < self.heap_array[left_idx]:
                    self.heap_array[head_idx], self.heap_array[left_idx] \
                        = self.heap_array[left_idx], self.heap_array[head_idx]
            else:
                if self.heap_array[left_idx] > self.heap_array[right_idx]:
                    if self.heap_array[head_idx] < self.heap_array[left_idx]:
                        return True
                    else:
                        return False
                else:
                    if self.heap_array[head_idx] < self.heap_array[right_idx]:
                        return True
                    else:
                        return False


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
print(heap.heap_array)
heap.insert(20)
print(heap.heap_array)
print(heap.delete())
print(heap.heap_array)
print(heap.delete())
print(heap.heap_array)
print(heap.delete())
