from unittest import TestCase
from top_k_largest import top_k_largest


class TestTopK(TestCase):
    def test_top_k_largest(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(5, top_k_largest(nums, k))
