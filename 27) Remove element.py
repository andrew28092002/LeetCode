class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, to_fill = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[to_fill] = nums[i]
                to_fill += 1
            i += 1
        return to_fill