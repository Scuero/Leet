class Solution(object):
    def addBinary(self, a, b):
        numero_a = int(a, 2)
        numero_b = int(b, 2)
        return bin(numero_a+numero_b)[2:]
        