"""
Getting the tree back from two lists that were 
obtained from traversing the tree in Inorder and Postorder,
respectively.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Recursive
def tree_from_inorder_postorder_rec(inorder, postorder):
    if not inorder or not postorder:
        return None
    else:
        root = TreeNode(postorder.pop())
        try:
            root_inorder_index = inorder.index(root.val)
        except:
            raise ValueError('Inorder and Postorder lists are incompatible.')
        root.right = tree_from_inorder_postorder_rec(inorder[root_inorder_index + 1:], postorder)
        root.left = tree_from_inorder_postorder_rec(inorder[:root_inorder_index], postorder)
        return root

# Iterative
from collections import deque

def tree_from_inorder_postorder_it(inorder, postorder):
    def search_inorder(the_list, s, e, val):
        i = s
        while i < e:
            if thelist[i] == val:
                return i
            i += 1
        return None
    if not inorder or not postorder:
        return None
    else:
        root = TreeNode(postorder[-1])
        try:
            in_index = inorder.index(root.val)
        except:
            raise ValueError('Inorder and Postorder lists are incompatible.')
        post_current_end = len(postorder)-1
        todo = deque() # Used as a stack
        todo.append((root, 'left', 0, in_index))
        todo.append((root, 'right', in_index + 1, len(inorder)))
        while todo:
            node, side, in_s, in_e = todo.pop()
            if in_s >= in_e or post_current_end < 0:
                setattr(node, side, None)
            else:
                new_node = TreeNode(postorder[post_current_end - 1])
                post_current_end -= 1
                setattr(node, side, new_node)
                new_in_pos = search_inorder(inorder, in_s, in_e, new_node.val)
                if new_in_pos == None:
                    raise ValueError('Inorder and Postorder lists are incompatible.')
                else:
                    todo.append((new_node, 'left', in_s, new_in_pos))
                    todo.append((new_node, 'right', new_in_pos + 1, in_e))
        return root
                
                
