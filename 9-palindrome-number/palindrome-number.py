class Solution(object):
    def isPalindrome(self, x):
        if x>=0:
            numero_invertido = int(str(x)[::-1])
            return (numero_invertido==x)
        return False
        