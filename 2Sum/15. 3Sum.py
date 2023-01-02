# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force way: must be 3 loops but will exceed time
        # easier way is to use sort+2pointer
        # there are duplicates in the array, how to get rid of the duplicates
        # we want to elimintae
        # sort first to eliminate duplicates
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                # means that we met duplicate, just skip this iteration
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res


sol = Solution()
res = sol.threeSum([-1, 0, 1, 2, -1, -4])
print(res)
