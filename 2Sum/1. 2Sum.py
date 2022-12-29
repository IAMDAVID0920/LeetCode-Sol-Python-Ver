# 2 sum is the basic question
# will paste the solution here
from typing import List


class Solution:
    # This is the brute force which will take O(N2) time
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # This is a better solution which cost O(N) because we use hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                # map[diff]will give us the index of value: diff
                # i will give us the index of nums[i] so we have 2 index been adding into the list
                return [map[diff], i]
            else:
                # otherwise, put current nums[i] and its index into the map
                map[nums[i]] = i


s = Solution()
res = s.twoSum([2, 7, 11, 15], 9)
res2 = s.twoSum([3, 2, 4], 6)
res3 = s.twoSum2([2, 7, 11, 15], 9)
res4 = s.twoSum2([3, 2, 4], 6)

print(f"res: {res}, res2: {res2}, res3: {res3}, res4: {res4}")
