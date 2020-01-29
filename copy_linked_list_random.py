"""
Program to deep copy a linked list with random pointer as well as next pointer
"""
from collections import OrderedDict


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def display(node1, node2):
    while node1 and node2:
        print(f'Node1: {node1.val}, {node1.random.val}')
        print(f'Node2: {node2.val}, {node2.random.val}')
        node1, node2 = node1.next, node2.next


def copy_list(node):
    """
    O(n) extra space solution
    :param node:
    :return:
    """
    curr = node
    map = OrderedDict()
    while curr is not None:
        if not map.get(curr, None):
            map[curr] = Node(curr.val)
        if curr.next and not map.get(curr.next, None):
            map[curr.next] = Node(curr.next.val)
            map[curr].next = map[curr.next]
        if curr.random and not map.get(curr.random, None):
            map[curr.random] = Node(curr.next.random)
            map[curr].random = map[curr.random]
        curr = curr.next
    display(node, next(iter(map)))


def clone(node):
    """
    O(1) space solution
    :param node:
    :return:
    """
    curr = node
    while curr is not None:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = curr.next.next

    curr = node
    while curr is not None:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    curr = node
    dup_root = node.next
    while curr.next is not None:
        temp = curr.next
        curr.next = curr.next.next
        curr = temp
    print('---------------------')
    display(node, dup_root)


if __name__ == '__main__':
    original_list = Node(1)
    original_list.next = Node(2)
    original_list.next.next = Node(3)
    original_list.next.next.next = Node(4)
    original_list.next.next.next.next = Node(5)

    '''Set the random pointers'''
    original_list.random = original_list.next.next
    original_list.next.random = original_list
    original_list.next.next.random = original_list.next.next.next.next
    original_list.next.next.next.random = original_list.next.next.next.next
    original_list.next.next.next.next.random = original_list.next

    copy_list(original_list)
    clone(original_list)