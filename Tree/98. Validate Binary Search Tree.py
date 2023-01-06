# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)

        return helper(root, float("-inf"), float("inf"))

    #  -inf< <inf -> -inf is left, inf is right, 5 is root.val
    #       5
    #-inf<3<5 -> on the left side: left will still be -inf, right will be the node.val
    #  3       5<7<inf on the right side: right will still be inf, left will be node.val
    #           7
    #
    #         4   8
    # that is why the logic is 
    # helper(node.left, left, node.val) and helper(node.right, node.val, right)
