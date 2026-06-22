# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        curr = dummy_head
        p1, p2 = list1, list2

        while p1 or p2:
            if not p2:
                curr.next = p1
                break
            if not p1:
                curr.next = p2
                break
            if p1.val == p2.val:
                tmp = p1.next
                curr.next = p1
                curr = curr.next
                curr.next = p2
                curr = curr.next
                p1 = tmp
                p2 = p2.next
            elif p1.val < p2.val:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next

        return dummy_head.next
        