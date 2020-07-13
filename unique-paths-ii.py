class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        v = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                v = 0
            dp[i][0] = v

        v = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                v = 0
            dp[0][j] = v

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

if __name__ == "__main__":
    #obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    #obstacleGrid = [[1, 1]]
    obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
    obstacleGrid = [[0,0],[1,0]]
    #obstacleGrid = [[1, 0]]
    s = Solution()
    print s.uniquePathsWithObstacles(obstacleGrid)
