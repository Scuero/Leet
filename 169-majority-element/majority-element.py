class Solution(object):
    def majorityElement(self, nums):
        dic = {}
        repeticiones = 0
        mayoria = 0
        for numero in nums:
            dic[numero] = dic.get(numero, 0) + 1
            if dic[numero] > repeticiones:
                repeticiones = dic[numero]
                mayoria = numero
        return mayoria

        