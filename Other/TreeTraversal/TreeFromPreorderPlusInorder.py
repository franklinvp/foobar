"""
Given two lists assumed to be obtained from traversing the
nodes of a tree in preorder and postorder, respectively, 
recover the tree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Recursive
def tree_from_preorder_inorder_rec(preorder, inorder):
    if not preorder or not inorder:
        return None
    else:
        root = TreeNode(preorder.pop(0))
        try:
            inorder_index = inorder.index(root.val)
        except:
            raise ValueError('Preorder and Inorder lists are incompatible')
        root.left = tree_from_preorder_inorder_rec(preorder, inorder[:inorder_index])
        root.right = tree_from_preorder_inorder_rec(preorder, inorder[inorder_index + 1:])
        return root

# Iterative
from collections import deque

def tree_from_preorder_inorder_it(preorder, inorder):
    def search_list(the_list, s, e, val):
        i = s
        while i < e:
            if the_list[i] == val:
                return i
            i += 1
        return None
    if not preorder or not inorder:
        return None
    else:
        root = TreeNode(preorder[0])
        pre_current_start = 1
        pre_length = len(preorder)
        try:
            in_index = inorder.index(root.val)
        except:
            raise ValueError('Preorder and Inorder lists are incompatible.')
        todo = deque()
        todo.append((root, 'right', in_index + 1, len(inorder)))
        todo.append((root, 'left', 0, in_index))
        while todo:
            node, side, in_s, in_e = todo.pop()
            if in_s >= in_e or pre_current)start >= pre_length:
                setattr(node, side, None)
            else:
                new_node = TreeNode(preorder[pre_current_start])
                setattr(node, side, new_node)
                pre_current_start += 1
                new_node_inorder_index = search_list(inorder, in_s, in_e, new_node.val)
                if new_node_inorder_index == None:
                    raise ValueError('Preorder and Inorder lists are not compatible.')
                else:
                    todo.append((new_node, 'right', new_node_inorder_index + 1, in_e))
                    todo.append((new_node, 'left', in_s, new_node_inorder_index))
        return root
