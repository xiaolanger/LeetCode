class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        numbers = [num for num in nums]
        numbers.sort(reverse=True)

        rankmap = {}
        rank = 1
        for num in numbers:
            if rank == 1:
                rankmap[num] = "Gold Medal"
            elif rank == 2:
                rankmap[num] = "Silver Medal"
            elif rank == 3:
                rankmap[num] = "Bronze Medal"
            else:
                rankmap[num] = str(rank)
            rank += 1

        return [rankmap[num] for num in nums] 

if __name__ == "__main__":
    # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
    l = [10,3,8,9,4]
    s = Solution()
    print s.findRelativeRanks(l)
