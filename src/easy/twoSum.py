""" 1. Two Sum
Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? """
from typing import List

class Solution:
    def twoSumHighHighComplexity(self, nums: List[int], target: int) -> List[int]:
        for n1 in range(0, len(nums), 1):
            for n2 in range(n1 + 1, len(nums), 1):
                if (nums[n1] + nums[n2] == target):
                    return [n1, n2]
                
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked: dict = {}
        for i, num, in enumerate(nums):
            missing: int = target - num
            if missing in checked:
                return [checked[missing], i]
            checked[num] = i

mySolution = Solution()

mySolution.twoSum(nums = [2,7,11,15], target = 9)

solutions = [
    {"nums": [2,7,11,15], "target": 9, "expected": [0,1]},
    {"nums": [3,2,4], "target": 6, "expected": [1,2]},
    {"nums": [3,3], "target": 6, "expected": [0,1]},
]


for solution in solutions:
    result = mySolution.twoSum(solution['nums'], solution['target'])
    assert result == solution['expected'], (
        f"Error: {solution['a']} + {solution['b']} "
        f"expected {solution['expected']} but got {result}"
    )

print("All tests passed")
