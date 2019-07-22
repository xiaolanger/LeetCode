class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        add = True
        for num in nums:
            if add:
                total += num
            add = not add
        return total

if __name__ == "__main__":
    l = [1,4,3,2]
    s = Solution()
    print s.arrayPairSum(l)
