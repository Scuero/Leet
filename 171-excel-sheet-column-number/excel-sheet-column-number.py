class Solution(object):
    def titleToNumber(self, columnTitle):
        suma = 0
        for columna in columnTitle:
            suma = suma * 26 + (ord(columna) - ord('A') + 1)
        return suma
        