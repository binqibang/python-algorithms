from unittest import TestCase
from binarysearch.search_min import search_min
from binarysearch.search_range import search_range


class Test(TestCase):

    def test_search_range(self):
        nums = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10]
        self.assertListEqual([1, 2], search_range(nums, 2))

    def test_search_min(self):
        nums = [8, 9, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(1, search_min(nums))
