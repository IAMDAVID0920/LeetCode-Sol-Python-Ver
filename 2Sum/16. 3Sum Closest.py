from typing import List
class Solution:
    # cannot use hashset since we don't have the specific target Value 
    # fix the first one, then use 2 pointer on the otherside
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        # [-1, 2, 1, -4] -> sort [-4, -1, 1, 2]
        res = nums[0] + nums[1] + nums[N - 1]
        nums.sort()

        for i in range(N - 2):
            left, right = i + 1, N -1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < abs(res - target):
                    res = sum
                if sum > target:
                    right -= 1
                else:
                    left += 1

        return res



sol = Solution()
res = sol.threeSumClosest([-1, 2, 1,-4], 1)
res2 = sol.threeSumClosest([0, 0, 0], 1)
print(res, res2)
