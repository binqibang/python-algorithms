from bt import TreeNode


def pre_order_traverse(root: TreeNode) -> list[int]:
    def dfs(root: TreeNode, lst: list[int]):
        if root is None:
            return
        lst.append(root.val)
        dfs(root.left, lst)
        dfs(root.right, lst)

    lst = []
    dfs(root, lst)
    return lst


def post_order_traverse(root: TreeNode) -> list[int]:
    stack = [(root, 0)]
    lst = []
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if not visited:
            stack.append((node, 1))
            stack.append((node.right, 0))
            stack.append((node.left, 0))
        else:
            lst.append(node.val)
    return lst


def in_order_traverse(root: TreeNode) -> list[int]:
    stack = [(root, 0)]
    lst = []
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if not visited:
            stack.append((node.right, 0))
            stack.append((node, 1))
            stack.append((node.left, 0))
        else:
            lst.append(node.val)
    return lst
