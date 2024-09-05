from unittest import TestCase
from top_k_frequent import top_k_frequent


class Test(TestCase):
    def test_top_k_frequent(self):
        res = top_k_frequent([3, 2, 3, 4, 2, 2], 2)
        self.assertEqual(set(res), {2, 3})
