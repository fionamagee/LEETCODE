class Solution(object):
    def climbStairs(self, n):
        dp = [0] * (n+1)

        for i in range(n,-1,-1):
            if i == n or i == n-1:
                dp[i] = 1
            else:
                dp[i] = dp[i+1] + dp[i+2]

        return dp[0]

            

        
