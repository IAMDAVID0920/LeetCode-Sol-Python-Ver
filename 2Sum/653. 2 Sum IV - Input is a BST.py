# Definition for a binary tree node 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def helper(root, k):
            if not root: return False
            if k - root.val in s: return True
            s.add(root.val)
            return(helper(root.left, k) or helper(root.right, k))
        return helper(root, k)

sol = Solution()
# res1 = sol.findTarget([5,3,6,2,4,None,7], 9)
# res2 = sol.findTarget([5,3,6,2,4,None,7], 28)

# print(res1, res2)
