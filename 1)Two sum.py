class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in index:
                return [i, index[remaining]]
            index[value] = i
