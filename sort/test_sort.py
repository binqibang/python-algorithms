from unittest import TestCase

from list import create_random_arr
from quick_sort import quick_sort
from merge_sort import merge_sort


class Test(TestCase):
    def test_quick_sort(self):
        for i in range(100):
            nums = create_random_arr(100)
            my_sort = quick_sort(nums)
            self.assertListEqual(sorted(nums), my_sort)

    def test_merge_sort(self):
        for i in range(10000):
            nums = create_random_arr(100)
            my_sort = merge_sort(nums)
            self.assertListEqual(sorted(nums), my_sort)