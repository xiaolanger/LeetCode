class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dp = [1 for i in range(l)]

        for i in range(1, l):
            big = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    big = max(big, dp[j] + 1)

            dp[i] = big

        result = 0
        for i in range(l):
            result = max(result, dp[i])

        return result

if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    nums = [10,9,2,5,3,4]
    print s.lengthOfLIS(nums)
