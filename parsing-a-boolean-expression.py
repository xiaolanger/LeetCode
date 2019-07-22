class Solution(object):
    def __init__(self):
        self.index = 0
        self.length = 0

    def getChar(self, expression):
        c = expression[self.index]
        self.index += 1
        return c

    def unGetChar(self, expression):
        c = expression[self.index]
        self.index -= 1
        return c

    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        self.length = len(expression)
        return self.parseLogic(expression)

    def parseParams(self, expression):
        result = []

        while True:
            c = self.getChar(expression)
            if c == '(' or c == ',':
                continue
            elif c == ')':
                break
            elif c == 't' or c == 'f':
                result.append(c == 't')
            else:
                self.unGetChar(expression)
                result.append(self.parseLogic(expression))

        return result

    def parseLogic(self, expression):
        c = self.getChar(expression)
        bs = self.parseParams(expression)

        result = not bs[0] if c == '!' else bs[0]

        for b in bs[1:]:
            if c == '&':
                result = result and b
            elif c == '|':
                result = result or b
            else:
                result = not b

        return result

if __name__ == "__main__":
    expr = "|(&(t,f,t),!(t))"
    expr1 = "!(f)"
    s = Solution()
    print s.parseBoolExpr(expr1)
