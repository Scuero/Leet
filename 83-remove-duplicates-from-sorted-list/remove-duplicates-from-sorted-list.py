# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        actual = head
        siguiente = head.next
        while (actual and siguiente):
            if (actual.val == siguiente.val):
                siguiente = siguiente.next
                actual .next = siguiente
            else:
                actual = siguiente
                siguiente = siguiente.next
        return head

        