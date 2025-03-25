class Solution(object):
    def plusOne(self, digits):
        total = 0
        for numero in digits:
            total = (total *10)+numero
        total += 1
        numero_string = str(total)
        return [int(digito) for digito in numero_string]
        