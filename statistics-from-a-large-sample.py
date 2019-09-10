class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        num = 0
        # small
        small = -1
        # big
        big = 0
        # mean
        totalCnt = 0
        totalSum = 0
        # mode
        mostCnt = 0
        mostNum = 0

        for cnt in count:
            if cnt != 0:
                # small
                if small == -1:
                    small = num
                # big
                big = num
            # mean
            totalCnt += cnt
            totalSum += num * cnt
            # mode
            if mostCnt < cnt:
                mostCnt = cnt
                mostNum = num
            num += 1

        # median
        indexs = []
        if totalCnt % 2 == 0:
            indexs = [(totalCnt - 1) / 2, totalCnt / 2]
        else:
            indexs = [totalCnt / 2, totalCnt / 2]

        num = 0
        index = 0
        median = -1
        for cnt in count:
            if index <= indexs[0] and indexs[0] < index + cnt:
                median = num

            if index <= indexs[1] and indexs[1] < index + cnt:
                median = (median + num) / 2.0

            index += cnt
            num += 1

        result = []
        result.append(small)
        result.append(big)
        result.append(totalSum * 1.0 / totalCnt)
        result.append(median)
        result.append(mostNum)

        return result

if __name__ == "__main__":
    # Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
    # l = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # l = [0,0,0,0,0,0,0,0,0,0,286,863,1452,1916,2486,3213,3482,4159,4695,5416,5782,6316,7024,7581,8029,8678,9174,9808,10249,10861,11374,11961,12577,13142,13750,13972,14621,15252,15597,16358,17025,17472,18164,18602,19163,19516,20287,20777,21119,21961,21911,22152,21147,20498,20284,19652,19304,18913,18645,17996,17426,17017,16635,16273,15837,15287,15028,14353,14102,13505,13229,12724,12105,11663,11250,11082,10247,10025,9405,9102,8506,8134,7926,7092,6918,6501,6140,5646,5037,4652,4344,3797,3371,2972,2489,1976,1479,1138,681,244,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    l = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,262,891,1386,1925,2553,3025,3571,4126,4740,5222,5807,6419,7021,7500,7992,8605,9335,9771,10217,10946,11360,11991,12534,12903,13595,13985,14923,15433,15787,16448,17093,17503,17902,18512,19299,19788,20372,21019,21546,22246,21777,21628,21054,20744,20053,20010,19268,18836,18422,17794,17666,17188,16560,16150,15853,15288,14938,14316,13938,13502,13152,12632,12233,11794,11343,10790,10375,10012,9503,8961,8673,8331,7764,7126,6838,6352,5996,5609,5221,4581,4185,3819,3326,2820,2398,2028,1604,1121,660,215,0,0,0,0,0,0,0,0,0,0,0]
    s = Solution()
    print s.sampleStats(l)
