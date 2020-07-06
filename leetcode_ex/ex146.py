from collections import deque

class LRUCache:
    '''
    考虑通过一个链表和一个字典来实现.
    '''
    def __init__(self, capacity: int):
        # 记录一个可用容量
        self.cap = capacity
        # map : key -> obj
        self.map = {}
        # priority_queue : obj=(value, offset)
        self.deque = deque()

    def get(self, key: int) -> int:
        v = self.map.get(key)
        if v is None or v[0] == -1:
            return -1

        k = v[0]
        new_v = [k]
        v[0] = -1
        self.deque.append(new_v)
        self.map[key] = new_v
        return new_v[0]

    def remove(self):
        old_obj = self.deque.popleft()
        while isinstance(old_obj, list) and old_obj[0] == -1 and len(self.deque) >= 0:
            old_obj = self.deque.popleft()
        old_obj[0] = -1

    def put(self, key: int, value: int) -> None:
        v = self.map.get(key)
        if v is None or v[0] == -1:
            if self.cap > 0:
                self.cap -= 1
            else:
                self.remove()
        else:
            v[0] = -1

        obj = [value]
        self.deque.append(obj)
        self.map[key] = obj


if __name__ == '__main__':
    ins = ["put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
    v = [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
     [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
     [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
     [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
     [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
     [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

    cache = LRUCache(10)
    for i in range(len(ins)):
        if ins[i] == "get":
            res = cache.get(*tuple(v[i]))
            print(res)
        else:
            cache.put(*tuple(v[i]))



