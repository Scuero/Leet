class Solution(object):
    def mySqrt(self, x):
        raiz = 1
        while ((raiz*raiz) < x):
            raiz += 1
        if raiz*raiz == x:
            return raiz
        else:
            return raiz-1
        