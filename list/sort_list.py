from typing import Optional

from list import ListNode, array2list, list2array


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    mid = middle(head)
    l1, l2 = head, mid.next
    mid.next = None
    l1 = sort_list(l1)
    l2 = sort_list(l2)
    return merge_two_lists(l1, l2)


def middle(head):
    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def merge_two_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    dummy = ListNode(0)
    prev = dummy
    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    if l1:
        prev.next = l1
    else:
        prev.next = l2
    return dummy.next


if __name__ == '__main__':
    head = array2list([3, 1, 2, 3, 5])
    print(list2array(sort_list(head)))
