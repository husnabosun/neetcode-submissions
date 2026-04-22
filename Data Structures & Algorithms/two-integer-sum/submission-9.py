class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in nums[i+1:]:
                new_nums = nums[i+1:]
                if difference == nums[i]:
                    return [i, new_nums.index(difference) + (i+1)]
                else: 
                    return [i, nums.index(difference)]