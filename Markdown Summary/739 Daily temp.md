# 739. Daily Temperature

[739. Daily Temperatures](https://leetcode.cn/problems/daily-temperatures/)

```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(N) and O(N)
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # stack[-1] which is stack.pop() in python, stack[-1][0] due to enumerate, there are 2 values
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            
            stack.append([temp, i])
        
        return res
```

```java
class Solution {
    public int[] dailyTemperatures(int[] T) {
        // O(N^2) and O(N) brute force
        int[] res = new int[T.length];
        for (int i = 0; i < T.length; i++) {
            for (int j =  i; j < T.length; j++) {
                if (T[j] > T[i]) {
                    // count the index difference
                    res[i] = j - i;
                    break;
                }
            }
        }
        return res;
    }
}
```

