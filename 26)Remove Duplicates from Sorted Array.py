class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        for i in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                nums.pop(index+1)
            else:
                index +=1
        return len(nums)
