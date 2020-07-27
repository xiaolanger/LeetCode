#There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item.
#
#What's the maximum value can you put into the backpack?

class Solution(object):
    def backPack(self, size, items, values):
        dp = [[0 for j in range(size + 1)] for i in range(len(items) + 1)]

        for i in range(1, len(items) + 1):
            for j in range(size + 1):
                if items[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1]] + values[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(items)][size]

if __name__ == "__main__":
    s = Solution()
    size = 10
    items = [2, 3, 5, 7]
    values = [1, 5, 2, 4]
    print s.backPack(size, items, values)
