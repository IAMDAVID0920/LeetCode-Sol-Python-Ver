# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # O(N2) because of the for loop
        # preorder [3,9,20,15,7]
        # inorder  [9,3,15,20,7]
        # output:  [[3,9,20,null,null,15,7]
        # if preorder[-1] inorder[-1] then output will be [-1] as well
        # preStart -> 0, inStart -> 1 means that 9 is the only one on the left
        N = len(preorder)
        def helper(preStart, inStart, inEnd):
            inIndex = 0
            if inStart > inEnd:     
                return None

            root = TreeNode(preorder[preStart])
            # the first one in preorder is the root, then find
            # what pos root at in inorder traversal, left is left, right is right
            for i in range(len(inorder)):
                if inorder[i] == root.val:
                    inIndex = i

            leftTreeSize = inIndex - inStart
            root.left = helper(preStart+1, inStart, inIndex - 1)
            root.right = helper(preStart+1+leftTreeSize, inIndex+1, inEnd)
            return root

        return helper(0, 0, N - 1)


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # easier solution
        # so if the preorder or inorder is empty?
        if not preorder or not inorder:
            return None

        # otherwise we are building the treenode now, root will be preorder[0]
        root = TreeNode(preorder[0])
        # how we split left and right? find the root in inorder
        mid = inorder.index(preorder[0])
        # then we came back and construct both left and right tree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # faster solution -> using hashmap to optimize from O N2 to O N
        # preorder will always let us to construct root, and
        # we will always grab root and see what the pos in the inorder array
        tmpMap = dict()
        preOrderIdx = 0
        N = len(preorder)
        for i in range(N):
            tmpMap[i] = i

        def helper(inStart, inEnd):
            if inStart > inEnd:
                return None
            
            preOrderIdx+=1
            root = TreeNode(preorder[preOrderIdx])
            idx = tmpMap[root.val]
            root.left = helper(inStart, index - 1)
            root.right = helper(index+1, inEnd)
            return root

        return helper(0, N - 1)

