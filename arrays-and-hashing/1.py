class Solution(object):
    def twoSum(self, nums, target):
        target_set = {}

        for i in range(len(nums)):
            if target - nums[i] in target_set:
                return [i , target_set[target - nums[i]]]
            target_set[nums[i]] = i


        
