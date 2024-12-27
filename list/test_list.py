from unittest import TestCase
from list import *
from list.merge_k_Lists import merge_k_lists
from my_lru import LRUCache


class Test(TestCase):
    def test_merge(self):
        lists = []
        for i in range(5):
            arr = sorted(create_random_arr(5))
            # print(arr)
            lists.append(array2list(arr))
        head = merge_k_lists(lists)
        merged = list2array(head)
        # if merged lists ascending
        self.assertEqual(all(merged[i] <= merged[i + 1] for i in range(len(merged) - 1)), True)

    def test_lru(self):
        lru = LRUCache(2)
        lru.set(1, 1)
        lru.set(2, 2)
        self.assertEqual(2, lru.get(2))
        lru.set(3, 3)
        self.assertEqual(-1, lru.get(1))
