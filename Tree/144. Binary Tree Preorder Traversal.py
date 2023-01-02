## Given the root of a binary tree, return the preorder traversal of its nodes' values 
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive way, normal way
        res = []

        def dfs(root):
            if root is None:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative way
        # use stack
        res = []
        stack = []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right
        
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative way preferred
        res, stack = [], []
        if root:
            stack.append(root)

        while stack:
            root = stack.pop()
            res.append(root.val)

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)


        return res
