class DoubleLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head = DoubleLinkedListNode(0, 0)
        self.tail = DoubleLinkedListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveFirst(node)
            return node.value
        else:
            return -1

    def moveFirst(self, node: DoubleLinkedListNode):
        self.remove(node)
        self.addFirst(node)

    def remove(self, node: DoubleLinkedListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addFirst(self, node: DoubleLinkedListNode):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new_node = DoubleLinkedListNode(key, value)
            self.cache[key] = new_node
            self.size += 1
            self.addFirst(new_node)
            if self.size > self.capacity:
                del self.cache[self.tail.prev.key]
                self.remove(self.tail.prev)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveFirst(node)
