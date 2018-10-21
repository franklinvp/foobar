def _visit(node):
    """
    Whatever needs to be done when visiting a node.
    For example, printing its satelite data.
    """
    print(node.val)

# Recursive
def preorder_rec(root):
    if root:
        _visit(root)
        preorder_rec(root.left)
        preorder_rec(root.right)

# Iterative
from collections import deque
def preorder_it(root):
    if root:
        todo = deque() # Used as a stack
        # Being on top of the stack means that it is ready to be 'visited'
        # when it is time to start visiting.
        todo.append(root)
        while todo:
            node = todo.pop()
            # Right goes first such that it is visited last.
            if node.right:
                todo.append(node.right)
            if node.left:
                todo.append(node.left)
            _visit(root)
