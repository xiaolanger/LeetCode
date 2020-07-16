class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dp = [0 for i in range(l)]

        dp[0] = 1

        for i in range(1, l):
            for j in range(i):
                if dp[j] != 0 and i - j <= nums[j]:
                    if dp[i] == 0:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = min(dp[j] + 1, dp[i])
                    break

        return dp[l - 1] - 1

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    s = Solution()
    print s.jump(nums)
