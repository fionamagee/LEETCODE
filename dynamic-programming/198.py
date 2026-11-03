class Solution(object):
    def rob(self, nums):
        dp = [0] * len(nums)

        if dp == []:
            return None

        for i in range(len(nums)):
            if i == 0 or i == 1:
                dp[i] = nums[i]
            elif i == 2:
                dp[i] = nums[i] + dp[0]
            else:
                dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        
        if len(dp) < 2:
            return dp[0]
        return max(dp[-1], dp[-2])
