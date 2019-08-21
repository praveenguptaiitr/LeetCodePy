class DLinkListNode:
    def __init__(self):
        self.key = None
        self.val = None
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.head = DLinkListNode()
        self.tail = DLinkListNode()
        self.size = 0
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head


    def _addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _removeNode(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._removeNode(node)
        self._addNode(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._removeNode(res)
        return res

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self.moveToHead(node)

        return node.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key)

        if not node:
            newNode = DLinkListNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self.moveToHead(node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache( 2 )

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)