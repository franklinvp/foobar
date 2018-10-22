"""
Height = Maximum length of a path between a leaf of the tree
         and the root.
"""

from collections import deque

def height_binary_tree(root):
    height = -1
    if not root:
        return height
    else:
        todo = deque() # Used as a queue
        todo.append(root)
        while True:
            level_size = len(todo)
            if level_size == 0:
                return height
            else:
                height += 1
            while level_size > 0:
                node = todo.popleft()
                if node.left:
                    todo.append(node.left)
                if node.right:
                    todo.append(node.right)
                level_size -= 1
