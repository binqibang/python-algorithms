from typing import Optional

from list import ListNode, array2list


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = dummy
    for i in range(n):
        fast = fast.next
        # invalid param n
        if not fast:
            return head

    slow = dummy
    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


if __name__ == '__main__':
    head = array2list([1, 2, 3, 4, 5])
    print(remove_nth_from_end(head, 6).val)
