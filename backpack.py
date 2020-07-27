# Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

class Solution(object):
    def backPack(self, size, items):
        dp = [[False for j in range(size + 1)] for i in range(len(items) + 1)]

        dp[0][0] = True

        for i in range(1, len(items) + 1):
            for j in range(size + 1):
                if items[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - items[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        for i in range(size, -1, -1):
            if dp[len(items)][i]:
                return i

        return 0

if __name__ == "__main__":
    s = Solution()
    items = [3,4,8,5]
    size = 10

#    items = [2,3,5,7]
#    size = 12
    print s.backPack(size, items)
