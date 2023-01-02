## Given the root of a binary tree, return the preorder traversal of its nodes' values 
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                # need to find greater place
                # find for right subtree
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                # find for left subtree
                cur = cur.left
            else:
                # otherwise the current node is the LCA
                return cur
