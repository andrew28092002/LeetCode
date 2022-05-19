class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)
        return max_sum