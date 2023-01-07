# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # There are 2 ways to solve this question:
    # first is the recursive way
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node, level):
            if not node:
                return []

            if level == len(res):
                res.append(node.val)

            dfs(node.right, level+1)
            dfs(node.left, level+1)

        dfs(root, 0)
        return res

    # this we use bfs to iterate (use stack)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = collections.deque([root]) 
        res = []
        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)

        return res
