class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target > nums[-1]: return len(nums)
        if target < nums[0]: return 0
        left = 0
        right = len(nums)-1
        while right >= left:
            mid = (left+right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return right + 1