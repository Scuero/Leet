class Solution(object):
    def minimumRecolors(self, blocks, k):
        maxConsecutivas = blocks[:k].count("B")
        for indice in range(len(blocks) - k):
            subStringSiguiente = blocks[indice+1:k+indice+1]
            cantidadNegrasSiguiente = subStringSiguiente.count("B")
            if (cantidadNegrasSiguiente>maxConsecutivas):
                maxConsecutivas = cantidadNegrasSiguiente
        return k-maxConsecutivas
