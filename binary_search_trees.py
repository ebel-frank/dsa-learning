"""
    Question: Write a function to check if a binary tree is a binary
    search tree

    Question: Write a function to find the maximum key in a binary tree

    Question: Write a function to find the minimum key in a binary tree
"""
from binary_tree import TreeNode


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = is_bst_l and is_bst_r and \
                  (min_l is None or node.key > min_l) and \
                  (max_r is None or node.key < max_r)

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return is_bst_node, min_key, max_key


class BSTNode(TreeNode):
    def __init__(self, key, value=None):
        super().__init__(key)
        self.value = value
        self.parent = None


def insert(node, key, value):
    if node is None:
        return BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    elif key < node.key:
        return find(node.left, key)
    elif key > node.key:
        return find(node.right, key)


def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height


def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, hi, root)

    return root


def balance_bst(node):
    return make_balanced_bst(list_all(node))


if __name__ == '__main__':
    # tree_tuple = (1, 2, 3)
    # tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    # tree = TreeNode.parse_tuple(tree_tuple)
    # print(is_bst(tree))
    #
    # tree2_tuple = (('aakash', "biraj", "hemanth"), "jadhesh", ("siddhant", "sonaksh", "vishal"))
    # tree2 = TreeNode.parse_tuple(tree2_tuple)
    # print(is_bst(tree2))

    # tree = insert(None, "jadhesh", "Jadhesh")
    # insert(tree, "biraj", "biraj")
    # insert(tree, "sonaksh", "sonaksh")
    # insert(tree, "aakash", "aakash")
    # insert(tree, "hemanth", "hemanth")
    # insert(tree, "siddhant", "siddhant")
    # insert(tree, "vishal", "vishal")
    # insert(tree, "tanya", "tanya")
    # tree.display_keys()
    #
    # # find a node
    # node = find(tree, "vishal")
    # print(node.key, node.value)
    #
    # print(list_all(tree))
    # print(is_balanced(tree))

    # data = [("jadhesh", "Jadhesh"), ("biraj", "biraj"), ("sonaksh", "sonaksh"),
    #         ("aakash", "aakash"), ("hemanth", "hemanth"), ("siddhant", "siddhant"),
    #         ("vishal", "vishal")]
    # tree = make_balanced_bst(data)
    # tree.display_keys()

    imbalanced_data = [("aakash", "aakash"), ("biraj", "biraj"), ("hemanth", "hemanth"),
                       ("jadhesh", "Jadhesh"), ("siddhant", "siddhant"), ("sonaksh", "sonaksh"),
                       ("vishal", "vishal")]
    tree1 = None
    for data in imbalanced_data:
        tree1 = insert(tree1, data[0], data[1])

    tree1.display_keys()

    tree2 = balance_bst(tree1)
    tree2.display_keys()
