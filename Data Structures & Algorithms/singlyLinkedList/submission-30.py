class LinkedList:
    
    def __init__(self):
        # dummy node
        self.head = LinkedNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

        
        

    def insertHead(self, val: int) -> None:
        new_node = LinkedNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

        

    def insertTail(self, val: int) -> None:
        self.tail.next = LinkedNode(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False



    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
       

class LinkedNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None