class Solution(object):
    def __init__(self):
        self.record = {}

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        return self.change(coins[::-1], amount)

    def change(self, coins, amount):
        count = -1

        if amount == 0:
            return 0

        if amount < 0:
            return -1

        for coin in coins:
            left = amount - coin

            if left in self.record:
                cnt = self.record[left]
            else:
                cnt = self.change(coins, left)
                self.record[left] = cnt

            if cnt != -1:
                if count == -1:
                    count = cnt + 1
                else:
                    count = min(cnt + 1, count)

        return count

if __name__ == "__main__":
    s = Solution()
    #coins = [1, 2, 5]
    #amount = 100

    coins = [186,419,83,408]
    amount = 6249

    print s.coinChange(coins, amount)
