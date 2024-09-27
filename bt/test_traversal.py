from unittest import TestCase
from bt import create_bt
from traversal import pre_order_traverse, in_order_traverse, post_order_traverse

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = create_bt(preorder, inorder)


class Test(TestCase):
    def test_pre_order_traverse(self):
        preorder = [3, 9, 20, 15, 7]
        self.assertListEqual(preorder, pre_order_traverse(root))

    def test_post_order_traverse(self):
        postorder = [9, 15, 7, 20, 3]
        self.assertListEqual(postorder, post_order_traverse(root))

    def test_in_order_traverse(self):
        inorder = [9, 3, 15, 20, 7]
        self.assertListEqual(inorder, in_order_traverse(root))