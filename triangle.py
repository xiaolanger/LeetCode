class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)

        for i in range(m - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]

if __name__ == "__main__":
    s = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    triangle = [[-1],[2,3],[1,-1,-3]]
    print s.minimumTotal(triangle)
