from typing import Optional

from list import ListNode


def isPalindrome(head: Optional[ListNode]) -> bool:
    if not head.next:
        return True
    fast, slow = head, head
    while fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse
    prev, curr = None, slow
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # compare
    p1, p2 = head, prev
    while p1 and p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True
