from typing import Optional

from list import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
