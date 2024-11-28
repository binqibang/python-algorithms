from typing import Optional

from list import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1:
        return l2
    if not l2:
        return l1
    carry = 0
    dummy = ListNode()
    prev = dummy
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        curr_sum = v1 + v2 + carry
        prev.next = ListNode(curr_sum % 10)
        carry = curr_sum // 10
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        prev = prev.next
    if carry:
        prev.next = ListNode(carry)
    return dummy.next
