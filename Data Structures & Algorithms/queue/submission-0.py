class Deque:
    
    def __init__(self):
        self.dummy_head = ListNode(0)
        self.dummy_tail = ListNode(0)
        self.dummy_tail.prev = self.dummy_head
        self.dummy_head.next = self.dummy_tail


    def isEmpty(self) -> bool:
        return self.dummy_tail.prev == self.dummy_head
        

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        new_node_prev = self.dummy_tail.prev
        new_node_next = self.dummy_tail

        new_node_prev.next = new_node
        new_node_next.prev = new_node
        new_node.prev = new_node_prev
        new_node.next = new_node_next
        

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        new_node_prev = self.dummy_head
        new_node_next = self.dummy_head.next

        new_node_prev.next = new_node
        new_node_next.prev = new_node
        new_node.prev = new_node_prev
        new_node.next = new_node_next
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        ret = self.dummy_tail.prev.val
        self.dummy_tail.prev.prev.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_tail.prev.prev
        return ret

        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        ret = self.dummy_head.next.val
        self.dummy_head.next.next.prev = self.dummy_head
        self.dummy_head.next = self.dummy_head.next.next
        return ret
        
        
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None