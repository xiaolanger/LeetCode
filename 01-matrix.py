class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        result = [[-1 for i in range(col)] for j in range(row)]

        queue = []
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r, c))

        index = 0
        while index < len(queue):
            r = queue[index][0]
            c = queue[index][1]

            distance = result[r][c] + 1
            # top
            if r - 1 >= 0:
                if result[r - 1][c] == -1 or result[r - 1][c] > distance:
                    result[r - 1][c] = distance
                    queue.append((r - 1, c))
            # bottom
            if r + 1 < row:
                if result[r + 1][c] == -1 or result[r + 1][c] > distance:
                    result[r + 1][c] = result[r][c] + 1
                    queue.append((r + 1, c))
            # left
            if c - 1 >= 0:
                if result[r][c - 1] == -1 or result[r][c - 1] > distance:
                    result[r][c - 1] = result[r][c] + 1
                    queue.append((r, c - 1))
            # right
            if c + 1 < col:
                if result[r][c + 1] == -1 or result[r][c + 1] > distance:
                    result[r][c + 1] = result[r][c] + 1
                    queue.append((r, c + 1))

            index += 1

        return result

if __name__ == "__main__":
    # matrix = [[0],[0],[0],[0],[0]]
    matrix = [[0,0,0],[0,1,0],[1,1,1]]

    s = Solution()
    print s.updateMatrix(matrix)
