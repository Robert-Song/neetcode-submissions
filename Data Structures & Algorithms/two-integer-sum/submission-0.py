class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val2index = dict()
        for i in range(len(nums)):
            if target - nums[i] in val2index:
                return [val2index[target - nums[i]], i]
            val2index[nums[i]] = i