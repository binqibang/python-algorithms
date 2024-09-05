class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import random


def create_random_arr(length: int) -> list:
    arr = []
    for i in range(length):
        arr.append(random.randint(1, 100))
    return arr


def array2list(nums: list) -> ListNode:
    dummy = ListNode()
    cur = dummy
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


def list2array(head: ListNode) -> list:
    curr = head
    arr = []
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr
