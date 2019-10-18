class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0] * (query_row + 1) for i in range(query_row + 1)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    dp[i + 1][j] += (dp[i][j] - 1) / 2.0
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2.0

        return min(1, dp[query_row][query_glass])

    def champagneTower1(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        row = 0
        p = poured
        mp = {}
        while row <= query_row:
            for r in range(row + 1):
                if row - 1 < 0:
                    p = poured
                elif r - 1 < 0:
                    p = mp[(row - 1, r)][1] / 2.0
                elif r > row - 1:
                    p = mp[(row - 1, r - 1)][1] / 2.0
                else:
                    p = (mp[(row - 1, r - 1)][1] + mp[(row - 1, r)][1]) / 2.0

                if p >= 1:
                    mp[(row, r)] = (1, p - 1)
                else:
                    mp[(row, r)] = (p, 0)

            row += 1

        return mp[(query_row, query_glass)][0]

if __name__ == "__main__":
    s = Solution()
    poured = 4
    query_glass = 0
    query_row = 3
    print s.champagneTower(poured, query_row, query_glass)
