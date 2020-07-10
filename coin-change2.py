class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = {}
        for i in range(amount + 1):
            dp[i] = amount + 1

        dp[0] = 0

        length = len(coins)
        for i in range(amount + 1):
            for j in range(length):
                left = i - coins[j]
                if left >= 0:
                    dp[i] = min(dp[i], dp[left] + 1)

        if dp[amount] <= amount:
            return dp[amount]

        return -1

if __name__ == "__main__":
    s = Solution()
    #coins = [1, 2, 5]
    #amount = 100

    coins = [186,419,83,408]
    amount = 6249

    print s.coinChange(coins, amount)
