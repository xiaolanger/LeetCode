import itertools

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.judgePoint(nums, 24)

    def judgePoint(self, nums, total):
        if len(nums) == 1:
            return abs(nums[0] - total) < 0.1 ** 6

        tups = list(itertools.permutations(nums, 2))
        for a, b in tups:
            leaves = [n for n in nums]
            leaves.remove(a)
            leaves.remove(b)

            r1 = self.judgePoint([a + b] + leaves, total)
            if r1:
                return r1

            r2 = self.judgePoint([a - b] + leaves, total)
            if r2:
                return r2

            r3 = self.judgePoint([a * b] + leaves, total)
            if r3:
                return r3

            r4 = False
            if b != 0:
                r4 = self.judgePoint([a * 1.0 / b] + leaves, total)
            if r4:
                return r4

        return False

if __name__ == "__main__":
    s = Solution()
    #nums = [4, 1, 8, 7]
    #print s.judgePoint24(nums)
    #nums = [1, 2, 1, 2]
    #print s.judgePoint24(nums)
    #nums = [5, 5, 5, 5]
    #print s.judgePoint24(nums)
    #nums = [5, 9, 5, 5]
    #print s.judgePoint24(nums)
    #nums = [1, 3, 4, 6]
    #print s.judgePoint24(nums)
    nums = [3, 3, 8, 8]
    print s.judgePoint24(nums)
    nums = [1, 1, 7, 7]
    print s.judgePoint24(nums)
