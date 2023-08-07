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

    def in_order_traversal(self):
        if self is None:
            return []
        return TreeNode.in_order_traversal(self.left) + [self.key] + TreeNode.in_order_traversal(self.right)

    def pre_order_traversal(self):
        if self is None:
            return []
        return [self.key] + TreeNode.pre_order_traversal(self.left) + TreeNode.pre_order_traversal(self.right)

    def post_order_traversal(self):
        if self is None:
            return []
        return TreeNode.post_order_traversal(self.left) + TreeNode.post_order_traversal(self.right) + [self.key]

    def display_keys(self, space='\t ', level=0):
        if self is None:
            print(space * level + '()')
            return

        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # if the node has children
        TreeNode.display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        TreeNode.display_keys(self.left, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), tree.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return f"BinaryTree <{self.to_tuple()}>"

    def __repr__(self):
        return f"BinaryTree <{self.to_tuple()}>"

    @staticmethod
    def parse_tuple(data):
        # print(data)
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node


if __name__ == "__main__":
    tree_tuple = (1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))
    tree = TreeNode.parse_tuple(tree_tuple)
    print(tree)
    # display_keys(tree)

    # Depth First Search or DFS
    # print(tree.in_order_traversal())
    # print(tree.pre_order_traversal())
    # print(tree.post_order_traversal())

    print(tree.height())
    print(tree.size())
