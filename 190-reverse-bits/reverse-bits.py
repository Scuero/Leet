class Solution:
    def reverseBits(self, n: int) -> int:
        binario = (bin(n)[2:].zfill(32))
        binario_reverso = [digito for digito in binario[::-1]]
        binario_reverso = "".join(binario_reverso)
        return int(binario_reverso,2)