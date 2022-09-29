# Sliding Window

## Template

```
//最长模板:
初始化left, right, result, bestResult
while (右指针没有到结尾) {
    窗口扩大, 加入right对应元素, 更新当前result
    while (result不满足要求) {
        窗口缩小, 移除left对应元素, left右移
    }
    更新最优结果bestResult
    right++;
}
返回bestResult;

```

```
//最短模板:
初始化left, right, result, bestResult
while (右指针没有到结尾) {
    窗口扩大, 加入right对应元素, 更新当前result
    while (result满足要求) {
        更新最优结果bestResult
        窗口缩小, 移除left对应元素, left右移
    }
    right++;
}
返回bestResult;
```



### 进 出 算

```java

public int lengthOfLongestSubstringKDistinct(String s, int k){
		Map<Character, Integer> map = new HashMap<>();
		int left = 0, res = 0;
  	for(int right = 0; right < s.length(); right++){
      char cur = s.charAt(right);
      map.put(cur, map.getOrDefault(cur, 0) + 1);
      while(map.size() > k){
        char c = s.charAt(left);
        map.put(c, map.get(c) - 1);
        if(map.get(c) == 0)		map.remove(c);
        left++;
      }
      res = Math.max(res, right - left + 1);
    }
  	return res;
}
```



### 3. Longest Substring without repeating chars

[3. Longest Substring without repeating chars](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

Idea: 滑动窗口的概念 2 pointers

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        int max = 0;
        Set<Character> window = new HashSet<>();
        
        while(right < s.length()){
            if(!window.contains(s.charAt(right))){
                window.add(s.charAt(right));
                right ++;
            }else{
                // if window contains s.charAt(right), then left move to right, remove far left element
                window.remove(s.charAt(left));
                left ++;
            }
            // At every end of loop, update the current maximum length
            max = Math.max(max, window.size());
        }
        return max;
    }
}
```

### 209. Minimize size subarray sum

[209. Minimize size subarray sum](https://leetcode.cn/problems/minimum-size-subarray-sum/submissions/)

Idea: 模板题 求最短

```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int right = 0;
        int sum = 0;
        int minLen = 0;
        while(right < nums.length){
            sum += nums[right];
            while(sum >= target){
                if(right - left + 1 < minLen || minLen == 0){
                    minLen = right - left + 1;
                }
                sum -= nums[left];
                left ++;
            }
            right ++;    
        }
        return minLen;
    }
}
```

### 76. Minimum Window Substring

[76. Minimum window substring](https://leetcode.cn/problems/minimum-window-substring/)

```java
class Solution {
    public String minWindow(String s, String t) {
        if(s == null || s.length() == 0)    return "";
        // create 2 hashmap
        Map<Character, Integer> window = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        int left = 0;
        int right = 0;
        // valid means that if the val of map is only 1 of that specific key
        int valid = 0;
        int len = Integer.MAX_VALUE;
        int start = 0;
        // Fill in with initialization on need Map
        // tMap: {
        //   A:1,
        //   B:1,
        //   C:1
        //        }
        // for(int i = 0; i < t.length(); i++){
        //     char tChar = t.charAt(i);
        //     tMap.put(tChar, tMap.getOrDefault(tChar, 0) + 1);
        // }
        char[] tChar = t.toCharArray();
        for(char c: tChar){
            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        }
        
        while(right < s.length()){
            char addChar = s.charAt(right);
            window.put(addChar, window.getOrDefault(addChar, 0) + 1);
            right ++;
            
            if(tMap.containsKey(addChar) && window.get(addChar).equals(tMap.get(addChar))){
               valid ++;
            } 
            
            while(valid == tMap.size()){
                // means that we need to shrink
                if(right - left < len){
                    len = right - left;
                    start = left;
                }
                char removeChar = s.charAt(left);
                // starts to shrink
                if(tMap.containsKey(removeChar) && window.get(removeChar).equals(tMap.get(removeChar))){
                    valid --;
                }
                
                window.put(removeChar, window.get(removeChar) - 1);
                left ++;
            }
        }
        
        return len == Integer.MAX_VALUE ? "" : s.substring(start, start + len);


    }
```

### 567. Permutation in String

[567. Permutation in String](https://leetcode.cn/problems/permutation-in-string/)

```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        Map<Character, Integer> need = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();
        // Store all s1 elements into the need map
        char[] s1arr = s1.toCharArray();
        for(char c : s1arr){
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        int left = 0;
        int right = 0;
        int valid = 0; // window中满足s1要求的字符个数

        while(right < s2.length()){
            char c = s2.charAt(right);
            ++right;
            if(need.containsKey(c)){
                window.put(c, window.getOrDefault(c, 0) + 1);
                if(window.get(c).equals(need.get(c))){
                    valid ++;
                }
            }

            if(right - left == s1.length()){
                if(valid == need.size()){
                    return true;
                }
                char d = s2.charAt(left);
                ++left;
                if(need.containsKey(d)){
                    if(window.get(d).equals(need.get(d))){
                        valid --;
                    }
                    window.put(d, window.get(d) - 1);
                }
            }
        }
        return false;
    }
}
```

### 239. Sliding Window Maximum

[239. Sliding Window Maximum](https://leetcode.cn/problems/sliding-window-maximum/)

Idea:Use Monotonic Queue Or Deque

**Java Deque API**

```
offer() -> insert
poll() -> 
peak() ->
pollLast() ->
peakLast() ->
pollFirst() ->
pollLast() ->

```

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // 双向队列
        ArrayDeque<Integer> window = new ArrayDeque<>();
        // store the final maximum answer
        int[] ans = new int[nums.length - k + 1];
        int index = 0;
        for(int i = 0; i < nums.length; i++){
            // queue head node suppose to be under [i - k + 1, i]
            while(!window.isEmpty() && window.peek() < i - k + 1){
                window.poll();
            }
            while(!window.isEmpty() && nums[window.peekLast()] < nums[i]){
                window.pollLast();
            }

            window.offer(i);

            if(i >= k -1 ){
                ans[index ++ ] = nums[window.peek()];
            }
        
        }
        return ans;
    }
}
```



### 121. Best Time to Buy and Sell Stock I

[121. Best Time to Buy and Sell Stock I](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Idea: **no need to check if left < right since left always on the left of right and we loop right. Keep moving right if array[right] < array[left], left = right, started from adding right and comparing with new left**

```java
class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 0;
        int max = 0;
        while(right < prices.length){
            if(prices[left] > prices[right]){
                left = right;
            }
            max = Math.max(max, prices[right] - prices[left]);
            right ++;
        }

        return max;
    }
}
```

### 122. Best Time to Buy and Sell Stock II

[122. Best Time to Buy and Sell Stock II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)

```java
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        for(int i = 1; i <= prices.length - 1; i++){
            if(prices[i] > prices[i - 1]){
                res += prices[i] - prices[i - 1];
            }
        }
        return res;

    }
}
```

