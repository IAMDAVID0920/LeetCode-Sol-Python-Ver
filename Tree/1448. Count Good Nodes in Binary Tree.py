# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(maxval, node):
            if not node:
                return 0
            
            res = 1 if node.val >= maxval else 0
            #then we gonna update the maxval
            maxval = max(node.val, maxval)

            res += helper(maxval, node.left)
            res += helper(maxval, node.right)

            return res
        return helper(root.val, root)


