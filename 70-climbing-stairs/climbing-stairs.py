class Solution(object):
    def climbStairs(self, n):
        pasoN_1 = 1
        pasoN_2 = 1
        for i in range(2, n+1):
            aux = pasoN_2
            pasoN_2 = pasoN_1
            pasoN_1 = pasoN_1 + aux
        return pasoN_1
        