def _visit(node):
    """
    Whatever needs to be done with the node when visited.
    For example, print its satelite data.
    """
    print(node.val)

# Recursive
def postorder_rec(root):
    postorder_rec(root.left)
    portorder_rec(root.right)
    _visit(root)

# Iterative
from collections import deque
def postorder_it(root):
    stack = deque()
    node = root
    while node or stack:
        # Left exploration.
        # Rights go into the stack.
        # Node goes into the stack immediately after its right.
        # This ordering tells us that its right needs further exploring.
        while node:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            node = node.left
        if stack:
            node = stack.pop()
            # Elements in the stack are ready to 'visit' except when
            # the left one its its right child. If so, then they
            # go back into the stack and the right child needs left exploration.
            if node.right and stack and node.right == stack[-1]:
                stack.pop()
                stack.append(node)
                node = node.right
            else:
                _visit(node)
                node = None
