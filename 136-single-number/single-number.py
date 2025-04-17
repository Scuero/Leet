class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for numero in nums:
            res = res^numero
        return res 