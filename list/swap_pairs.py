from typing import Optional

from list import ListNode, array2list


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    dummy = ListNode(0, head)
    p1, p2, p3 = dummy, head, head.next
    while p2 and p3:
        next = p3.next
        p1.next = p3
        p3.next = p2
        p2.next = next
        p1 = p2
        p2 = next
        if p2:
            p3 = p2.next
    return dummy.next


if __name__ == '__main__':
    head = array2list([1, 2, 3, 4])
    swap_pairs(head)
