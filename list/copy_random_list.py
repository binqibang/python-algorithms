from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    复制一个带有随机指针的链表。

    :param head: 原始链表的头节点。
    :return: 复制后的链表的头节点。
    """
    # 创建一个字典来存储原节点和克隆节点之间的映射关系
    list_map = dict()
    ptr = head
    while ptr:
        # 在字典中为每个原节点创建一个对应的克隆节点，克隆节点的值与原节点相同
        list_map[ptr] = Node(ptr.val)
        ptr = ptr.next

    ptr = head
    while ptr:
        # 设置克隆节点的next指针，指向原节点的next对应的克隆节点
        list_map[ptr].next = list_map[ptr.next] if ptr.next else None
        # 设置克隆节点的random指针，指向原节点的random对应的克隆节点
        list_map[ptr].random = list_map[ptr.random] if ptr.random else None
        ptr = ptr.next
    # 返回原头节点对应的克隆节点，作为新链表的头节点
    return list_map[head]

