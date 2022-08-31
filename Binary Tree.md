# Binary Tree

### Preorder

[144. Binary Tree Preorder Traversal](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

#### Idea: root, left, right

#### 迭代就要有个Stack 不停往左下压栈，左下Node为None之后一个一个pop栈顶Node，往右下再找。

Iterative Solution

```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right

        return res
```

Recursive Solution

```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```

### Inorder

[94. Binary Tree Inorder Traversal](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

#### Idea: left, root, right

Iterative Solution

#### 画个图就清楚了 要先无脑往左走 压栈 走不动了 先pop最底下的 然后加进result list里面 之后再往右边找

```python
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

```

Recursive Solution

```python
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
```

### Postorder

[145. Binary Tree Postoder Traversal](https://leetcode.cn/problems/binary-tree-postorder-traversal/)

Iterative Solution

```python
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        while root or stack:
            if root:
                # keep to right
                res.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop().left

        return res[::-1]
```

Recursive Solution

```python
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```

---

---



### Level Order Traversal -> BFS, Queue 层序遍历

[102. Binary Tree Level Order Traversal](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

#### Idea: 用Queue存每一层的Node List存每一层Node的left、right *value*， 生成时先把root存进queue

Iterative Solution

```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res
        q = collections.deque()
        q.append(root)
        while q:
            temp_res = []
            for _ in range(len(q)):
                cur = q.popleft()
                temp_res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            res.append(temp_res)
        return res
```

Recursive Solution

```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # recursive, use dfs
        res = []

        def dfs(root, depth):
            # depth means the level number in Binary Tree
            if not root: return []
            if len(res) == depth: res.append([])
            res[depth].append(root.val)

            if root.left: dfs(root.left, depth + 1)
            if root.right: dfs(root.right, depth + 1)

        dfs(root, 0)
        return res
```

### Level Order Traversal 2

[107. Binary Tree Level Order Traversal II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/)

#### Idea: Just same with Level Order Traverse 1, just need to reverse the list at last

Iterative Solution

```python
def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal, reverse list at last
        res = []
        if not root: return res
        q = collections.deque([root])
        while q:
            tmp_res = []
            for _ in range(len(q)):
                cur = q.popleft()
                tmp_res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(tmp_res)   

        return res[::-1]
```

[199. Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view/)

#### Idea: Find all right view means that every last node.val in corresponding level

Iterative Solution

```python
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs but only add right val (which is the last node value on that level)
        res = []
        if not root: return res
        q = collections.deque([root])
        while q:
            # give a variable on len(q) since the size of queue will change
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if i == size - 1:
                    res.append(cur.val)
        return res
```

Recursive Solution

```
...
```

[637. Average of Levels in Binary Tree](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)

#### Idea: Find every level node.val, put in a list, get the average by doing sum(lst) / len(lst)

Iterative Solution

```python
def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # get the sum of level node values and get the average( sum(lst) / len(lst) )

        res = []
        if not root: return res
        q = collections.deque([root])
        while q:
            level_lst = []
            for _ in range(len(q)):
                cur = q.popleft()
                level_lst.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            res.append(sum(level_lst) / len(level_lst))  
        
        return res
```

Recursive Solution

```
...
```

[429. N-ary Tree Level Order Traversal](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/)

#### Idea: same with level order traversal of binary tree, just need to loop through all the children in corresponding level

Iterative Solution

```python
def levelOrder(self, root: 'Node') -> List[List[int]]:
        # N-ary tree, add children in queue one by one 多个for loop去找children其余没区别
        res = []
        if not root: return res
        q = collections.deque([root])
        while q:
            size = len(q)
            level_lst = []
            for _ in range(size):
                cur = q.popleft()
                level_lst.append(cur.val)
                for child in cur.children:
                    q.append(child)
            res.append(level_lst)
        return res
```

Recursive Solution

```
...
```



[515. Find Largest Value in Each Tree Row](https://leetcode.cn/problems/find-largest-value-in-each-tree-row/)

#### Idea: Same with 102, just get max value in each level

Iterative Solution

```python
def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # find largest number in each level, store in a list and find max
        res = []
        if not root:
            return res
        q = collections.deque([root])
        while q:
            level_lst = []
            for _ in range(len(q)):
                cur = q.popleft()
                level_lst.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(max(level_lst))
        return res

```

Recursive Solution

```
...
```

[116. Popular Next Right Pointers in Each Node](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

#### Idea: 遇到每层最后一个node之前 先全都连起来 最后一个肯定指向null

Iterative Solution

```python
def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.left:        q.append(cur.left)
                if cur.right:       q.append(cur.right)
                # when not reaching to the last node, connect all previous nodes
                if i < size - 1:    cur.next = q[0]
            # At last, let the final node point to None
            cur.next = None
        return root
```

Recursive Solution

```
...
```

[117. Popular Next Right Pointers in Each Node II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/submissions/)

#### Idea: No difference with 116.

Iterative Solution

```python
def connect(self, root: 'Node') -> 'Node':
        if not root:                return root
        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if i < size - 1:    cur.next = q[0]
                if cur.left:        q.append(cur.left)
                if cur.right:       q.append(cur.right)

            cur.next = None
        return root 
```

[104. Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

#### idea: Iterate through nodes in level order, everytime we finished a level, cnt++

Iterative Solution

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        if not root:            return cnt
        # bfs to get the number of levels in the binary tree
        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.left:    q.append(cur.left)
                if cur.right:   q.append(cur.right)
            cnt += 1
        return cnt
```

Recursive Solution (1 line)

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # cnt = 0
        # if not root: return cnt
        # # bfs to get the number of levels in the binary tree
        # cnt = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # return cnt
```

[111. Minimum Depth of Binary Tree](https://leetcode.cn/problems/minimum-depth-of-binary-tree/submissions/)

#### Idea: 递归要check special cases (一直往左下↙或者一直往右下↘), (still 102变种 记一个level变量更新层数) 用bfs遍历 当遇到第一个node没有左右child的时候就可以返回当前level数了 否则就一直bfs遍历下去

Iterative Solution

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        if not root:                                return level
        q = collections.deque([root])
        level += 1
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if not cur.left and not cur.right:  return level
                if cur.left:                        q.append(cur.left)
                if cur.right:                       q.append(cur.right)
            level += 1
        return level
```

Recursive Solution

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:                        return 0
        if not root.left and root.right:    return 1 + self.minDepth(root.right)
        if not root.right and root.left:    return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```



---



### Invert Binary Tree

[226. Invert Binary Tree](https://leetcode.cn/problems/invert-binary-tree/)

#### Idea: Iterative is using queue to reverse on every level, Recursive will be start with root and go left and right.

Iterative Solution

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 					return root
        q = collections.deque([root])
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left: 	q.append(cur.left)
                if cur.right: q.append(cur.right)
        return root
```

Recursive Solution

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # directly do the swap start with root node
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```



---

### Symmetric Tree

[101. Symmetric Tree](https://leetcode.cn/problems/symmetric-tree/)

#### Idea: check left right with the right left and left left with right right :)

Iterative Solution

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = collections.deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            leftn = q.popleft()
            rightn = q.popleft()
            if not leftn and not rightn:
                # means current is symmetric
                continue
            if not leftn or not rightn or leftn.val != rightn.val:
                # Not symmetric
                return False
            # symmetric adding
            q.append(leftn.left)
            q.append(rightn.right)
            # symmetric adding
            q.append(leftn.right)
            q.append(rightn.left)
        return True
```

Recursive Solution

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # left is None, right, then return False
        # left, right is None, then return False
        # left is None and right is None, return True
        # left and right and left.val != right.val, return False
        # compare left.right with right.left or compare left.left with right.right
        def dfs(left, right):
            if not left and right: return False
            elif left and not right: return False
            elif not left and not right: return True
            elif left.val != right.val: return False
            outside = dfs(left.left, right.right)
            inside = dfs(left.right, right.left)
            return outside and inside
        return dfs(root.left, root.right)
```

### Count Complete Tree Nodes

[222. Count Complete Tree Nodes](https://leetcode.cn/problems/count-complete-tree-nodes/)

#### Idea: BFS, update cnt

Iterative Solution

```python
def countNodes(self, root: Optional[TreeNode]) -> int:
        # use bfs and a counter to update the number of nodes
        cnt = 0
        if not root:            return cnt
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                cnt += 1
                if cur.left:    q.append(cur.left)
                if cur.right:   q.append(cur.right)
        return cnt
```

Recursive Solution

#### 递归更简单。。跟找max path类似 别忘了count+1 因为root也算进去

```python
def countNodes(self, root: Optional[TreeNode]) -> int:
        # use bfs and a counter to update the number of nodes
        cnt = 0
        if not root:            return cnt
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

### Balanced Binary Tree

[110. Balanced Binary Tree](https://leetcode.cn/problems/balanced-binary-tree/)

#### Idea: Every Node need to be checked if the difference of left and right <= 1, not only from the root

Recursive Solution

```python
def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:        return True 
        def height(root):
            if not root:    return 0
            return 1 + max(height(root.left), height(root.right))

        lefth = height(root.left) + 1
        righth = height(root.right) + 1

        if abs(lefth - righth) <= 1:    
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
```

### Binary Tree Paths

[257. Binary Tree Paths](https://leetcode.cn/problems/binary-tree-paths/)

#### Idea: Backtracking, if node no l and no r, that is the ending case in one level of recursion, otherwise just keep checking left and right. Also can use stack to do it iteratively.

Iteratrive Solution (Stack + dfs)

```python
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = [(root, "")]
        if not root:    return res
        while stack:
            node, strr = stack.pop()
            if not node.left and not node.right:
                res.append(strr + str(node.val))
            if node.left:
                stack.append((node.left, strr + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, strr + str(node.val) + "->"))
        return res
```



Recursive Solution

```python
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if not root:        return paths
        if not root.left and not root.right:
            return [str(root.val)]
        # divide by left and right to solve side by side
        if root.left:
            for i in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + "->" + i)
        if root.right:
            for i in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + "->" + i)
        return paths
```

### Count Good Nodes in Binary Tree

[1448. Count Good Nodes in Binary Tree](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/)

#### Idea: -> keep a maxValue variable, everytime compare current node.val with maxValue

Recursive Solution dfs 

```python
def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:    return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)

```

### Same Tree

[100. Same Tree](https://leetcode.cn/problems/same-tree/)

#### Idea: Check root situation: not p not q-> true, p and q and p.val == q.val -> recursion, otherwise return false

Recursive Solution

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
```

### Sum of Left Leaves

[404. Sum of Left Leaves](https://leetcode.cn/problems/sum-of-left-leaves/)

#### Idea: Check what to do if we find the left node, we add the value to the sum, then keep recursion to find it.

Recursive Solution

```python
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # dfs return sum of all left leaves
        total = 0
        if not root:                            return total
        if not root.left and not root.right:    return total
        # check if the node is left node, if it is then add up the sum
        # if only get with left node
        if root.left and not root.left.left and not root.left.right:   
            total += root.left.val
        # otherwise keep recursion until meet the situation above
        return total + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
```

### Find Bottom Left Tree View

[513. Find Bottom Left Tree View](https://leetcode.cn/problems/find-bottom-left-tree-value/)

#### Idea: Use BFS + Queue, get each level number list, append the first one each time (first one since that is the left most under that corresponding level)

Iterative Solution

```python
def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # bfs? find last row and get the left most which is the first one in q level
        res = []
        if not root:            return 0
        q = collections.deque([root])
        while q:
            level_lst = []
            for i in range(len(q)):
                cur = q.popleft()
                level_lst.append(cur.val)
                if cur.left:    q.append(cur.left)
                if cur.right:   q.append(cur.right)
            res.append(level_lst[0])
        return res[ len(res) - 1 ]

# Better BFS way, just keep track of first item in the level, until reach to the last level

def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # bfs? find last row and get the left most which is the first one in q level
        res = 0
        if not root:            return 0
        q = collections.deque([root])
        while q:
            for i in range(len(q)):
                if i == 0:      res = q[0].val
                cur = q.popleft()
                if cur.left:    q.append(cur.left)
                if cur.right:   q.append(cur.right)
        return res
```

Recusrive Solution

```python
# Keep track 2 variable: maxLen and maxLen.left.val
# Use Backtracking
def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        curVal = curHeight = 0
        def dfs(node, height) -> None:
            if node is None:
                return
            height += 1
            dfs(node.left, height)
            dfs(node.right, height)
            nonlocal curVal, curHeight
            if height > curHeight:
                curHeight = height
                curVal = node.val
        dfs(root, 0)
        return curVal
```

### Path Sum

[112. Path Sum](https://leetcode.cn/problems/path-sum/)

#### Idea: dfs keep minus the current node.val with target sum, until target-node.val == 0

Recursive Solution

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs
        if not root:
            return False
        
        def dfs(root, targetSum):
            if not root:                
                return False
            if not root.left and not root.right and targetSum - root.val == 0:
                return True
            remain = targetSum - root.val
            # Use or because any one path achieved, it will return True
            return dfs(root.left, remain) or dfs(root.right, remain)

        return dfs(root, targetSum)
```

Iterative Solution

#### Idea: Use a stack to store path and current sum value of node.

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # stack
        stack = []
        if not root: return False
        stack.append((root, root.val))
        while stack:
            node, pathSum = stack.pop()
            size = len(stack)
            if not node.left and not node.right and pathSum == targetSum:
                return True
            if node.left:                           
                stack.append((node.left, pathSum + node.left.val))
            if node.right:                          
                stack.append((node.right, pathSum + node.right.val))
        
        return False
```

### Path Sum II

[113. Path Sum II](https://leetcode.cn/problems/path-sum-ii/)

#### Idea: Similar to Path Sum 112

Iterative Solution

Use 2 queues to track, one is for the loop, another is to track current sum and path list

```python
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # record a path list
        if not root: return []
        q, pathq = collections.deque([root]), collections.deque([(root.val, [root.val])])
        res = []
        while q:
            for _ in range(len(q)):
                curNode = q.popleft()
                val, path = pathq.popleft()
                if not curNode.left and not curNode.right and val == targetSum:
                    res.append(path)
                if curNode.left:
                    q.append(curNode.left)
                    pathq.append((curNode.left.val + val, path + [curNode.left.val]))
                if curNode.right:
                    q.append(curNode.right)
                    pathq.append((curNode.right.val + val, path + [curNode.right.val]))
        return res
```

Recursive Solution

```python
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # record a path list
        res = []
        path = []
        def dfs(root, remain):
            if not root: return []
            if not root.left and not root.right:
                if remain == 0: 
                    res.append(path.copy())
            if root.left:
                path.append(root.left.val)
                dfs(root.left, remain - root.left.val)
                path.pop()
            if root.right:
                path.append(root.right.val)
                dfs(root.right, remain - root.right.val)
                path.pop()
        if not root: return []
        path.append(root.val)
        dfs(root, targetSum - root.val)
        return res
```

### 105&106. Construct Binary Tree (Pre&In Post&In)

#### Idea: Postorder 结尾是root.val, Preorder 开头是root.val, Inorder 必不可少因为把root.left and root.right完美分隔开, 取到root之后 取in的左边右边 然后再去取pre/post的左边右边 继续递归取, 最后return root node

[106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

```python
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:   return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        separate_index = inorder.index(root_val)
        left_part = inorder[:separate_index]
        right_part = inorder[separate_index+1:]

        postorder_left = postorder[:len(left_part)]
        postorder_right = postorder[len(left_part): len(postorder) - 1]

        root.left = self.buildTree(left_part, postorder_left)
        root.right = self.buildTree(right_part, postorder_right)

        return root
```

[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/)

```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Similar to 105, just need to get first one from preorder to declare root
        if not preorder: return None
        root_val = preorder[0]
        root = TreeNode(root_val)

        idx = inorder.index(root_val)

        inLeftPart = inorder[:idx]
        inRightPart = inorder[idx+1:]

        # first one is root, skip
        preLeftPart = preorder[1:1+len(inLeftPart)]
        preRightPart = preorder[1+len(inLeftPart):]

        root.left = self.buildTree(preLeftPart, inLeftPart)
        root.right = self.buildTree(preRightPart, inRightPart)

        return root
```

### Merge two binary trees

[617. Merge 2 Binary Trees](https://leetcode.cn/problems/merge-two-binary-trees/)

#### Idea: 先root再左右，用个新root存merged binary tree

```python
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        if root1 and not root2:     return root1
        if not root1 and root2:     return root2

        # if root1 and root2, have another root to be the merged root
        root3 = TreeNode(root1.val + root2.val)
        # Use recursion to deal the root3.left and root3.right
        root3.left = self.mergeTrees(root1.left, root2.left)
        root3.right = self.mergeTrees(root1.right, root2.right)

        return root3
```

### Search in a Binary Search Tree

[700. Search in a binary search tree](https://leetcode.cn/problems/search-in-a-binary-search-tree/)

#### Idea: if root.val == val return root, then recursive on left or right, which one valid return which root

```python
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:    return None
        if root.val == val: return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)

def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 为什么要有返回值: 
        #   因为搜索到目标节点就要立即return，
        #   这样才是找到节点就返回（搜索某一条边），如果不加return，就是遍历整棵树了。

        if not root or root.val == val: 
            return root

        if root.val > val: 
            return self.searchBST(root.left, val)

        if root.val < val: 
            return self.searchBST(root.right, val)
```

### Validate BST

[98. Validate BST](https://leetcode.cn/problems/validate-binary-search-tree/)

#### Idea: 中序遍历 必须是升序 就是True

Iterative Solution

```python
def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        pre = None
        while cur or stack:
            if cur: # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else: # 逐一处理节点
                cur = stack.pop()
                if pre and cur.val <= pre.val: # 比较当前节点和前节点的值的大小
                    return False
                pre = cur 
                cur = cur.right
        return True
```

Recursive Solution

```python
def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur_max = -float("INF")
        def __isValidBST(root: TreeNode) -> bool: 
            nonlocal cur_max
            if not root: 
                return True
            is_left_valid = __isValidBST(root.left)
            if cur_max < root.val: 
                cur_max = root.val
            else: 
                return False
            is_right_valid = __isValidBST(root.right)
            
            return is_left_valid and is_right_valid
        return __isValidBST(root)
```

### Minimum Absolute Difference in BST

[530. Minimum Absolute Difference in BST](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)

```python
def getMinimumDifference(self, root: TreeNode) -> int:
        res = []   
        r = float("inf")
        def buildaList(root):
            if not root:        return None
            if root.left:       buildaList(root.left)
            res.append(root.val)
            if root.right:      buildaList(root.right)
            return res
            
        buildaList(root)
        for i in range(len(res)-1):
            r = min(abs(res[i]-res[i+1]),r)
        return r
```

### Find Mode in BST

[501. Find Mode in BST](https://leetcode.cn/problems/find-mode-in-binary-search-tree/)

```python
def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # BST 想inorder traversal
        res = []
        if not root: return res
        if not root.left and not root.right:    return [root.val]
        def inorder(root):
            if not root:        return None
            if root.left:       inorder(root.left)
            res.append(root.val)
            if root.right:      inorder(root.right)
            return res
        inorder(root)
        hm = {}
        for val in res:
            if val not in hm:
                hm[val] = 1
            else:
                hm[val] += 1
        return [key for key in hm.keys() if hm[key] == max(hm.values())]

```

### Lowest Common Ancestor of a Binary Tree

[236. Lowest Common Ancestor Binary Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

Recursive Solution

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # postorder traversal. From bottom to top
        if not root:                  return root
        if root == p or root == q:    return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:            return root
        if left and not right:        return left
        # if not left and right
        else:                         return right
```



### Lowest Common Ancestor of a Binary Search Tree

[235. Lowest Common Ancestor BST](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/)

Iterative Solution

```python
# 根据搜索树的特点，如果 p，q 值 都 < root 的值，就去左子树
# 根据搜索树的特点，如果 p，q 值 都 > root 的值，就去右子树
# 否则就是说分布在 root的左右子树中
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
```

Recursive Solution

```python
# 根据搜索树的特点，如果 p，q 值 都 < root 的值，就去左子树
# 根据搜索树的特点，如果 p，q 值 都 > root 的值，就去右子树
# 否则就是说分布在 root的左右子树中
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
```

### Insert into a BST

[701. Insert into a BST](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)

```python
def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:  
            # if 没有root 那么val就是新root的node val
            node = TreeNode(val)
            return node   
        # if val < root.val 往左放 otherwise往右放 搜到为空 就插入 return root
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root          
```

### Delete Node in a BST

[450. Delete Node in a BST](https://leetcode.cn/problems/delete-node-in-a-bst/)

```python
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # if 没找到
        if not root:        
            return root
        # recursion 继续左右找
        if root.val < key :
            root.right = self.deleteNode(root.right, key)
        elif root.val > key :
            root.left = self.deleteNode(root.left, key)
        else:
            # 当前节点的左子树为空，返回当前的右子树
            if not root.left : return root.right
            # 当前节点的右子树为空，返回当前的左子树
            if not root.right: return root.left
            # 左右子树都不为空，找到右孩子的最左节点 记为p
            node = root.right
            while node.left :
                node = node.left
            # 将当前节点的左子树挂在p的左孩子上
            node.left = root.left
            # 当前节点的右子树替换掉当前节点，完成当前节点的删除
            root = root.right
        return root
```

### Convert BST to a greater tree

[538. Convert BST to a greater tree](https://leetcode.cn/problems/convert-bst-to-greater-tree/)

Recursive Solution

```python
def __init__(self):
        self.pre=TreeNode()
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:    return None
        self.convertBST(root.right)
        self.pre.val+=root.val
        root.val=self.pre.val
        self.convertBST(root.left)
        return root
```

Iterative Solution

```
```

### Convert Sorted Array to BST

[](()

```PYTHON
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.traversal(nums, 0, len(nums) - 1)
        return root

    def traversal(self, nums: List[int], left: Optional[int], right: Optional[int]):
        if left > right:    return None
        mid = left + (right - left) // 2
        mid_root = TreeNode(nums[mid])
        mid_root.left = self.traversal(nums, left, mid - 1)
        mid_root.right = self.traversal(nums, mid + 1, right)

        return mid_root
```

