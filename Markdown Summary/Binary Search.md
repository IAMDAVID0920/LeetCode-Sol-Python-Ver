#  Binary Search

### Search in a Sorted Array of Unknown Size

[702. Search in a Sorted Array of Unknown Size](https://leetcode.cn/problems/search-in-a-sorted-array-of-unknown-size/)

#### Idea: 先找到valid size 大小 然后从 left = size//2, right = size 开始二分

```python
def search(self, reader: 'ArrayReader', target: int) -> int:
        l, r = 0, 1
        while reader.get(r) < target:
            l = r
            r *= 2
        
        l = r // 2
        while l <= r:
            mid = l + (r - l) // 2
            if reader.get(mid) < target:
                l = mid + 1
            elif reader.get(mid) > target:
                r = mid - 1
            else:
                return mid
            
        return -1
```



