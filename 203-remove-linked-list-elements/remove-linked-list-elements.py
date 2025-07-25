# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        listaTemporal = ListNode(0, head)
        nodoActual = head
        nodoAnterior = listaTemporal
        while nodoActual:
            if nodoActual.val == val:
                nodoAnterior.next = nodoActual.next
            else:
                nodoAnterior = nodoActual
            nodoActual = nodoActual.next
        return listaTemporal.next
