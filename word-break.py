class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        mp = {}
        max_len = 0
        for word in wordDict:
            max_len = max(max_len,len(word))
            mp[word] = True

        l = len(s)
        dp = [False for i in range(l + 1)]
        for i in range(1, max_len + 1):
            if s[0:i] in mp:
                dp[i] = True

        for i in range(1, l + 1):
            for j in range(i):
                if dp[j] and s[j:i] in mp:
                    dp[i] = True

        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]

#    s = "applepenapple"
#    wordDict = ["apple", "pen"]

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    print solution.wordBreak(s, wordDict)
