class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.least, self.most = ListNode(), ListNode()
        self.least.next = self.most
        self.most.prev = self.least


    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        self.moveNode(self.cache[key])
        return self.cache[key].val

    
    def moveNode(self, node):
        # remove current node first if already in the list
        if node.prev and node.next:
            curr = node
            curr_prev = curr.prev
            curr_next = curr.next
            curr_prev.next = curr_next
            curr_next.prev = curr_prev

        # insert at tail
        new_next = self.most
        new_prev = self.most.prev
        node.next = new_next
        node.prev = new_prev
        new_next.prev = node
        new_prev.next = node
    
    def removeLeastUsed(self):
        lru = self.least.next
        lru_prev = lru.prev
        lru_next = lru.next
        lru_prev.next = lru_next
        lru_next.prev = lru_prev
        del self.cache[lru.key]


    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            new_node = ListNode(value, key)
            self.cache[key] = new_node
        else:
            self.cache[key].val = value
        self.moveNode(self.cache[key])

        if len(self.cache) > self.capacity:
            self.removeLeastUsed()


        
class ListNode:
    def __init__(self, val=0, key=-1):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None