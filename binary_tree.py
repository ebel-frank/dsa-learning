"""
    Question: Implement a binary tree using python and show it's usage
    with some examples
"""


class TreeNode:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)


def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def tree_to_tuple(tree: TreeNode):
    if tree.left is None and tree.right is None:
        return tree.key
    if tree.left is not None:
        left = tree_to_tuple(tree.left)
    else:
        left = None
    if tree.right is not None:
        right = tree_to_tuple(tree.right)
    else:
        right = None
    return left, tree.key, right


def display_keys(node, space='\t ', level=0):
    if node is None:
        print(space * level + '()')
        return

        # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

        # if the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)


def in_order_traversal(node):
    if node is None:
        return []
    return in_order_traversal(node.left) + [node.key] + in_order_traversal(node.right)


if __name__ == "__main__":
    tree_tuple = (1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))
    tree = parse_tuple(tree_tuple)
    print(tree.left.key)
    print(tree.right.key)
    print(tree_to_tuple(tree))
    # display_keys(tree)
    print(in_order_traversal(tree))
