class DoublyLinkedListNode:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.least = DoublyLinkedListNode()
        self.most = DoublyLinkedListNode()
        self.least.next = self.most
        self.most.prev = self.least

        self.capacity = capacity

        self.items = {}

    def insert(self, node):
        prev = self.most.prev

        prev.next = node
        node.prev = prev

        node.next = self.most
        self.most.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.items:
            self.remove(self.items[key])
            self.insert(self.items[key])
            return self.items[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.remove(self.items[key])
        self.items[key] = DoublyLinkedListNode(key, value)
        self.insert(self.items[key])

        if len(self.items) > self.capacity:
            lru = self.least.next
            self.remove(lru)
            del self.items[lru.key]
