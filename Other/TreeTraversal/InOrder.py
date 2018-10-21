def _visit(node):
    # Whatever the traversal needs to do with the node.
    # For example, print its satelite data.
    print(node.val)

# Recursive
def inorder_rec(root):
    inorder_rec(root.left)
    _visit(root.val)
    inorder_rec(root.right)

# Iterative
from collections import deque

def inorder_it(root):
    stack = deque()
    node = root
    # Having a node in hand means that it needs to be explored.
    # Having stuff in the stack means that we know of stuff that
    #     needs to be 'visited'.
    while node or stack: 
        # Explore to the left greedily.
        while node:
            stack.push(node)
            node = node.left
        # In this state we 'visit' from the stack and move
        #     once to the right.
        if not node and stack:
            node = stack.pop()
            _visit(node)
            node = node.right
