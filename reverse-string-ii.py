class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        p = 0
        result = ""
        reverse = True

        while p < len(s):
            if p + k < len(s):
                if reverse:
                    result += s[p + k - 1:p - 1:-1] if p > 0 else s[k - 1::-1]
                else:
                    result += s[p:p + k]
            else:
                if reverse:
                    result += s[len(s):p - 1:-1] if p > 0 else s[len(s)::-1]
                else:
                    result += s[p:]

            reverse = not reverse
            p += k

        return result

    def reverseStr1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            return s[::-1]

        if len(s) > k and len(s) < 2 * k:
            return s[k - 1::-1] + s[k:]

        return s[k - 1::-1] + s[k:2 * k] + self.reverseStr1(s[2 * k:], k)

if __name__ == "__main__":
    s = Solution()
    string = "abcdefg"
    print s.reverseStr(string, 2)
    print s.reverseStr1(string, 2)

    string = "abcd"
    print s.reverseStr(string, 4)
    print s.reverseStr1(string, 4)
