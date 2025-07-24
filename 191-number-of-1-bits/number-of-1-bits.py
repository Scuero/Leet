class Solution:
    def hammingWeight(self, n: int) -> int:
        cont = 0

        for i in range(31):
            #Shiftear siempre se aplica al numero en representacion binaria
            if (n >> i) & 1:
                cont += 1

        return cont