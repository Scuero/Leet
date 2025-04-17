class Solution(object):
    def singleNumber(self, nums):
        res = []
        for numero in nums:
            if numero not in res:
                res.append(numero)
            else:
                res.remove(numero)
        return res[0]
        