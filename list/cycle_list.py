from typing import Optional

from list import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    if head.next == head:
        return True
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return False
    if head.next == head:
        return True
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            ptr = head
            while ptr != slow:
                ptr = ptr.next
                slow = slow.next
            return slow
    return None
