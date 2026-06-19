class MyLinkedList:

    def __init__(self):
        self.dummy_head = LinkedNode(-1)
        self.dummy_tail = LinkedNode(-1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        

    def get(self, index: int) -> int:
        curr = self.dummy_head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.dummy_tail and index == 0:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = LinkedNode(val)
        new_node_prev = self.dummy_head
        new_node_next = self.dummy_head.next

        new_node_prev.next = new_node
        new_node_next.prev = new_node
        new_node.prev = new_node_prev
        new_node.next = new_node_next
        

    def addAtTail(self, val: int) -> None:
        new_node = LinkedNode(val)
        new_node_next = self.dummy_tail
        new_node_prev = self.dummy_tail.prev

        new_node_next.prev = new_node
        new_node_prev.next = new_node
        new_node.prev = new_node_prev
        new_node.next = new_node_next
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy_head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            new_node = LinkedNode(val)
            new_node_prev = curr.prev
            new_node_next = curr

            new_node_prev.next = new_node
            new_node_next.prev = new_node
            new_node.prev = new_node_prev
            new_node.next = new_node_next



    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy_head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0 and curr!= self.dummy_tail:
            curr_next = curr.next
            curr_prev = curr.prev

            curr_next.prev = curr_prev
            curr_prev.next = curr_next
            


class LinkedNode:
    def __init__(self, val: int):
        self.prev = None
        self.val = val
        self.next = None 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)