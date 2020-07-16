class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastGoodIndex = len(nums)-1
        for i in reversed(range(0,len(nums)-1)):
            if i + nums[i] >= lastGoodIndex:
                lastGoodIndex = i

        return lastGoodIndex == 0

#    def canJump(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: bool
#        """
#        l = len(nums)
#        dp = [False for i in range(l)]
#
#        dp[0] = True
#
#        for i in range(1, l):
#            for j in range(i - 1, -1, -1):
#                if dp[j] and i - j <= nums[j]:
#                    dp[i] = True
#                    break
#
#        return dp[l - 1]

if __name__ == "__main__":
    nums = [2,3,1,1,4]
#    nums = [3,2,1,0,4]
    s = Solution()
    print s.canJump(nums)
