class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.validPalindrome1(s, False)

    def validPalindrome1(self, s, delete):
        head = 0
        tail = len(s) - 1

        while head <= tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
                continue

            if not delete:
                if head + 1 <= tail and self.validPalindrome1(s[head + 1:tail + 1], True):
                    return True

                if head <= tail - 1 and self.validPalindrome1(s[head:tail], True):
                    return True

            return False

        return True

if __name__ == "__main__":
    s = Solution()
    print s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
    print s.validPalindrome("abc")
