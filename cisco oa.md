# Cisco OA 2022

### Get mode from a list

```python
def mode(ls):
    # dictionary to keep count of each value
    counts = {}
    # iterate through the list
    for item in ls:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for key in counts.keys():
        if counts[key] == max(counts.values()):
            return key
```

### Rotate Image

[48. Rotate Image](https://leetcode.cn/problems/rotate-image/)

```python
def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # first swap from left to right
        for i in range(n // 2):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

        # then swap from left bottom to right top using the diagnal line
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```



### N-Queens

[51. N-Queens](https://leetcode.cn/problems/n-queens/)

```python
def solveNQueens(self, n: int) -> List[List[str]]:
        if not n: return []
        board = [['.'] * n for _ in range(n)]
        res = []
        def isVaild(board,row, col):
            #判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            # 判断左上角是否冲突
            i = row -1
            j = col -1
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否冲突
            i = row - 1
            j = col + 1
            while i>=0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtracking(board, row, n):
            # 如果走到最后一行，说明已经找到一个解
            if row == n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
            for col in range(n):
                if not isVaild(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(board, row+1, n)
                board[row][col] = '.'
        backtracking(board, 0, n)
        return res
```

### Maximum Subarray

[53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/)

```python
def maxSubArray(self, nums: List[int]) -> int:
        temp = nums[0]
        trackSum = 0
        for num in nums:
            trackSum += num
            if trackSum < num:     trackSum = num
            if trackSum > temp:     temp = trackSum
        return temp
```

### Word Search

[79. Word Search](https://leetcode.cn/problems/word-search/)

```python
def exist(self, board, word):
        row, col = len(board), len(board[0])

        def dfs(x, y, index):
            if board[x][y] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            board[x][y] = '#'
            for choice in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + choice[0], y + choice[1]
                if 0 <= nx < row and 0 <= ny < col and dfs(nx, ny, index + 1):
                    return True
            board[x][y] = word[index]

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False

```

### Counting 1 Bits

[191. Count 1 bits](https://leetcode.cn/problems/number-of-1-bits/)

```python
def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
```

### Decode Ways

[91. Decode Ways](https://leetcode.cn/problems/decode-ways/)

```java
class Solution {
    public int numDecodings(String s) {
        return process(s, 0);
    }
    public int process(String s, int i) {
        if (i == s.length()) {
            return 1;
        }
        if (s.charAt(i) == '0') {
            return 0;
        }
        if (s.charAt(i) == '1') {
            int res = process(s, i + 1);
            if (i + 1 < s.length()) {
                res += process(s, i + 2);
            }
            return res;
        }
        if (s.charAt(i) == '2') {
            int res = process(s, i + 1);
            if (i + 1 < s.length() && s.charAt(i + 1) >= '0' && s.charAt(i + 1) <= '6') {
                res += process(s, i + 2);
            }
            return res;
        }
        return process(s, i + 1);
    }
}
```

### Validate IP Address

[468. Validate IP Address](https://leetcode.cn/problems/validate-ip-address/)

```python
def validIPAddress(self, queryIP: str) -> str:
        def isIPV4(queryIP):
            v4Lst = queryIP.split('.')
            if len(v4Lst) != 4: return False
            for num in v4Lst:
                if not num:                         return False
                if not num.isdecimal():             return False
                if num[0] == '0' and len(num) != 1: return False
                if int(num) < 0 or int(num) > 255:  return False
            return True

        def isIPV6(queryIP):
            validIPv6 = "0123456789abcdefABCDEF"
            if "::" in queryIP:                     return False
            v6Lst = queryIP.split(':')
            if len(v6Lst) != 8:                     return False
            for num in v6Lst:
                if not num:                         return False
                if len(num) > 4:                    return False
                for n in num:
                    if n not in validIPv6:          return False
            return True


        if '.' in queryIP and isIPV4(queryIP):
            return "IPv4"
        elif ':' in queryIP and isIPV6(queryIP):
            return "IPv6"
        else:
            return "Neither"
```

### Custom Sorted Array

```python
CUSTOM SORTED ARRAY

In an array, elements at any two indices can be swapped in a single operation called a move. For example, if the array is arr = [17, 4, 8], swap arr[0] = 17 and arr[2] = 8 to get arr' = [8, 4, 17] in a single move. Determine the minimum number of moves required to sort an array such that all of the even elements are at the beginning of the array and all of the odd elements are at the end of the array.

Example
arr = [6, 3, 4, 5]

The following four arrays are valid custom-sorted arrays:

a = [6, 4, 3, 5]
a = [4, 6, 3, 5]
a = [6, 4, 5, 3]
a = [4, 6, 5, 3]
The most efficient sorting requires 1 move: swap the 4 and the 3.

Function Description
Complete the function moves in the editor below.

moves has the following paramenters(s):
int arr[n]: an array of positive integers

Returns
int: the minimum number of moves it takes to sort an array of integers with all even elements at earlier indices than any odd element

Note: The order of the elements within even or odd does not matter.

Constraints

2 <= n <= 10 ^ 5
1 <= arr[i] <= 10 ^ 9, where 0 <= i < n.
It is guaranteed that array contains atleast one even and one odd element.

public int minSwapsToSort(int[] nums) {
        int count = 0; // min number of swaps to sort
        int evenCount = 0; //even count

        for (int num: nums) {
            if (isEven(num))
                evenCount++;  // count even elements
        }

        for (int i = 0; i < evenCount; i++) {   // evenCount are the only elements we need to focus on
            int value = nums[i];

            if (isOdd(value))  // So, this is not in place
                count++;
        }

        return count;
    }

    private boolean isOdd(int num) {
        return (num % 2 == 1);
    }

    private boolean isEven(int num) {
        return (num % 2 == 0);
    }
```