from datetime import datetime

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [[0 for i in range(2001)] for j in range(len(nums))]
        dp[0][nums[0] + 1000] += 1
        dp[0][-nums[0] + 1000] += 1

        for i in range(1, len(nums)):
            for j in range(-1000, 1001):
                if dp[i - 1][j + 1000] != 0:
                    dp[i][j - nums[i] + 1000] += dp[i - 1][j + 1000]
                    dp[i][j + nums[i] + 1000] += dp[i - 1][j + 1000]

        return dp[len(nums) - 1][S + 1000]

    def findTargetSumWays2(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        queue = [0]
        pos = 0

        while pos < len(nums):
            temp = []
            for i in [-nums[pos], nums[pos]]:
                for j in queue:
                    temp.append(j + i)
            queue = temp
            pos += 1

        return len(filter(lambda x: x == S, queue))

    def findTargetSumWays1(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 0:
            return 1 if S == 0 else 0

        return self.findTargetSumWays1(nums[1:], S - nums[0]) + self.findTargetSumWays1(nums[1:], S + nums[0])
        
if __name__ == "__main__":
    s = Solution()

    #nums = [1, 1, 1, 1, 1]
    #S = 3

    #nums = [1, 0]
    #S = 1

    nums = [27,22,39,22,40,32,44,45,46,8,8,21,27,8,11,29,16,15,41,0]
    S = 10

    start = datetime.now()
    print s.findTargetSumWays(nums, S)
    end = datetime.now()
    print end - start

    start = datetime.now()
    print s.findTargetSumWays2(nums, S)
    end = datetime.now()
    print end - start

    start = datetime.now()
    print s.findTargetSumWays1(nums, S)
    end = datetime.now()
    print end - start
