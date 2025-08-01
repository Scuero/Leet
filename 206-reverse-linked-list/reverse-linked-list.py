# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next    # Guardo el siguiente
            curr.next = prev    # Ahora el nodo siguiente al nodo actual, sera el anterior
            prev = curr         # Luego de invertir, cambio el nodo anterior y actual
            curr = temp

        return prev