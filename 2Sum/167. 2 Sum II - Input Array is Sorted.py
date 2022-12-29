from typing import List


class Solution:
    # Follow up: if number is really big -> overflow? Use Long!
    # Follow up2: If target is double? check target-tmp < 0.01
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in map:
                # Simply adding a check
                if map[diff] > i:
                    return [i+1, map[diff]+1]
                else:
                    return [map[diff]+1, i+1]
            else:
                map[numbers[i]] = i
        return None

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use 2 pointer to do it because the array is already sorted
        left, right = 0, len(numbers) - 1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp == target:
                return [left+1, right+1]
            elif tmp > target:
                # if greater than target, we move the right cursor to left
                right -= 1
            else:
                # if smaller than target, we move the left cursor to right
                left += 1
        return None

s = Solution()
res = s.twoSum([2, 7, 11, 15], 9)
res2 = s.twoSum([2, 3, 4], 6)
res3 = s.twoSum2([2, 7, 11, 15], 9)
res4 = s.twoSum2([2, 3, 4], 6)

print(res, res2, res3, res4)
