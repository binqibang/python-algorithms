from typing import Optional

from list import ListNode


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    cnt = 0
    ptr = head
    while ptr:
        cnt += 1
        ptr = ptr.next
    if cnt < k:
        return head

    prev, curr = head, head.next

    for i in range(k - 1):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head.next = reverse_k_group(curr, k)

    return prev
