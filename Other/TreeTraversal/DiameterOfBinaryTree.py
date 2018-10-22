"""
Diameter = maximum length of a (simple is automatic for being a tree) path 
between two nodes.
"""

from collections import deque

def diameter_binary_tree(root):
    if not root:
        return -1 # The diameter of the empty tree coult be defined as -1, 0, or -float('inf').
    else:
        todo = deque() # Used as a stack
        todo.append(root)
        done = dict() # Can be replaced by marks on the nodes.
        while todo:
            node = todo.pop()
            lh, ld, rh, rd = -1, -1, -1, -1 # Left and Right height and diameters.
            if (node.right and node.right not in done) \
               or (node.left and node.left not in done):
                todo.append(node)
                if node.right:
                    todo.append(node.right)
                if node.left:
                    todo.append(node.left)
            else:
                if node.right:
                    rh, rd = done[node.right]
                if node.left:
                    lh, ld = done[node.left]
                # Keep track of the height and diameter of the subtree of each node.
                # Height is one more than the maximum of the heights of the 
                #     left and right subtrees.
                # The diameter is the maximum between the diameter of the left
                #     subtree, the right subtree, and the sum of the height to the left
                #     and the height to the right.
                done[node] = (max(lh, rh)+1, max(ld, rd, (lh+1) + (rh+1))) 
        return done[root][1]
