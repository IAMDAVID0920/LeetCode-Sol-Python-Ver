# Third dummy file for testing PyGithub PR diff
# This file can be deleted after testing

from typing import List, Optional


def find_max(numbers: List[int]) -> Optional[int]:
    """Find the maximum number in a list."""
    if not numbers:
        return None
    return max(numbers)


def find_min(numbers: List[int]) -> Optional[int]:
    """Find the minimum number in a list."""
    if not numbers:
        return None
    return min(numbers)


def calculate_average(numbers: List[int]) -> Optional[float]:
    """Calculate the average of numbers in a list."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Max: {find_max(nums)}")
    print(f"Min: {find_min(nums)}")
    print(f"Average: {calculate_average(nums)}")

