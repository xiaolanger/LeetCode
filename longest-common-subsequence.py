class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        inf = 0
        dp = [ [inf for j in range(len(text2) + 1)] for i in range(len(text1) + 1) ]

        dp[0][0] = 0
        dp[0][1] = 0
        dp[1][0] = 0

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]

if __name__ == "__main__":
    s = Solution()
    #text1 = "abcde"
    #text2 = "ace"
    text1 = "ezupkr"
    text2 ="ubmrapg"
    print s.longestCommonSubsequence(text1, text2)
