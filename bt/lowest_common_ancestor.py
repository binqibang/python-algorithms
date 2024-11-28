from bt import TreeNode, create_bt


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the lowest common ancestor of two nodes in a binary tree.
    :param root: The root node of the binary tree.
    :param p: The first node.
    :param q: The second node.
    :return: The lowest common ancestor node of p and q.
    """
    if not root:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    elif not left:
        return right
    else:
        return left


if __name__ == '__main__':
    # 一棵二叉树的前序和中序遍历，节点在10个
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = create_bt(preorder, inorder)
    p = root.left
    q = root.right.right
    lowest_common_ancestor(root, p, q)
