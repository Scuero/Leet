class Solution(object):
    def convertToTitle(self, columnNumber):
        res = []
        while(columnNumber > 0):
            columnNumber -= 1
            act = columnNumber % 26
            columnNumber = int(columnNumber / 26)
            res.append(chr(act + ord('A')))
        
        return ''.join(res[::-1])
        