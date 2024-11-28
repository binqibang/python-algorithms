from . import ListNode


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    return merge(lists, 0, len(lists) - 1)


def merge(lists, start, end):
    if start > end:
        return None
    if start == end:
        return lists[start]
    mid = (start + end) // 2
    l1 = merge(lists, start, mid)
    l2 = merge(lists, mid + 1, end)
    return merge_two_lists(l1, l2)


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
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
