class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split("/")
        record = []
        for p in paths:
            if p == '.' or p == '':
                pass
            elif p == '..':
                if len(record) > 0:
                    record.pop()
            else:
                record.append(p)

        return "/" + "/".join(record)

if __name__ == "__main__":
    s = Solution()
    print s.simplifyPath("/a/./b/../../c/")
