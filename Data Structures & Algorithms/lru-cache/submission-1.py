class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    def insert(self, node):
            prev = self.right.prev
            nxt = self.right

            prev.next = node
            nxt.prev = node

            node.prev = prev
            node.next = nxt
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            evict = self.left.next
            self.remove(evict)
            del self.cache[evict.key]
            

