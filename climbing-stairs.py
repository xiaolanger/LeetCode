class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(50)]

        dp[1] = 1
        dp[2] = 2

        for i in range(3, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
        
if __name__ == "__main__":
    n = 3
    s = Solution()
    print s.climbStairs(n)
