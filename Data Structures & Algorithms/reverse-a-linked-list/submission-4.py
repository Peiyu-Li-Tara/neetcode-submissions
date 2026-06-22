# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iteratively:
        # dummy_head = ListNode()

        # while head:
        #     tmp = head.next
        #     head.next = dummy_head.next
        #     dummy_head.next = head
        #     head = tmp
        
        # return dummy_head.next

        # recursively
        if not head:
            return None
        

        # maintail the new head
        new_head = head
        if new_head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        # if the head happens to be the first node of the list, we set its next to None
        head.next = None
        return new_head
