"""

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
reversed_alphabet_dict = {k: v for k, v in zip(alphabet, reversed(alphabet))}

def solution(encrypted_str)
    result = ""
    for v in encrypted_str:
        result+=reversed_alphabet_dict.get(v, v)"""


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def generate_tree_po(height, nums):
    if height == 1:
        return Node(nums.pop())

    node = Node(nums.pop())
    node.right = generate_tree_po(height-1, nums)
    node.left = generate_tree_po(height-1, nums)
    return node


height = 3
tree = generate_tree_po(height, list(range(1, 2 ** height)))


def find_parent_po(node, value):
    if node is not None:
        # Traverse the left and right subtrees
        yield from find_parent_po(node.left, value)
        yield from find_parent_po(node.right, value)
        # Yield the value of the current node
        if node.left and (node.left.value == value or node.right.value == value):
            yield node


def find_parents(values):
    result = []
    for value in values:
        x = [node.value for node in find_parent_po(tree, value)]
        result.append(x[0]) if x else -1
    return result
