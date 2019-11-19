class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True

        queue = [2, 3, 5]
        while len(queue) > 0:
            d = queue.pop(0)
            while num % d == 0:
                num = num / d

        return num == 1
                
if __name__ == "__main__":
    s = Solution()
    print s.isUgly(6)
    print s.isUgly(8)
    print s.isUgly(14)
