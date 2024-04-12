class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for record in nums:
            for number in range(len(nums)):
                if nums.index(record) != number and (record + nums[number]) == target:
                    return [nums.index(record),number]
