import queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    ENTER_ROOT_MSG = "Enter value of root node: "

    check = check_terminator(ENTER_ROOT_MSG)
    if check is None:
        return
    q = queue.Queue()
    tree_node = TreeNode(int(check))
    q.put(tree_node)

    while not q.empty():
        node_found = q.get()

        enter_left_reminder = f"Enter the left node of {node_found.data}: "
        check = check_terminator(enter_left_reminder)
        if check is None:
            return tree_node
        node_found.left = TreeNode(int(check))
        q.put(node_found.left)

        enter_right_reminder = f"Enter the right node of {node_found.data}: "
        check = check_terminator(enter_right_reminder)
        if check is None:
            return tree_node
        node_found.right = TreeNode(int(check))
        q.put(node_found.right)


def check_terminator(msg):
    TERMINATOR = 'n'
    check = input(msg).strip().lower() or TERMINATOR
    if check == TERMINATOR:
        return None
    else:
        return check


def pre_order(node: TreeNode) -> None:
    if not isinstance(node, TreeNode) or not node:
        return
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if not isinstance(node, TreeNode) or not node:
        return
    pre_order(node.left)
    print(node.data)
    pre_order(node.right)


def post_order(node):
    if not isinstance(node, TreeNode) or not node:
        return
    pre_order(node.left)
    pre_order(node.right)
    print(node.data)
