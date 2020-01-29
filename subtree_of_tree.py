class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_subtree(t: Node, s: Node):
    if t is None and s is None:
        return True
    if t is None or s is None:
        return False
    return t.data == s.data and check_subtree(t.left, s.left) and check_subtree(t.right, s.right)


def is_subtree(t: Node, s: Node) -> bool:

    if s is None:
        return True
    if t is None:
        return False
    if check_subtree(t, s):
        return True
    return is_subtree(t.left, s) or is_subtree(t.right, s)


if __name__ == "__main__":
    T = Node(26)
    T.right = Node(3)
    T.right.right = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)

    """
    creating second tree
    """
    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)

    print(is_subtree(T, S))