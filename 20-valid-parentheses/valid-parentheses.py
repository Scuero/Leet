class Solution(object):
    def isValid(self, s):
        pares_de_simbolos = {'(': ')', '[': ']', '{': '}'}
        pila = []
        for simbolo in s:
            if simbolo in pares_de_simbolos:
                pila.append(simbolo)
            if simbolo in pares_de_simbolos.values():
                if len(pila)==0:
                    return False
                simbolo_apertura = pila.pop()
                if simbolo != pares_de_simbolos[simbolo_apertura]:
                    return False
        return len(pila)==0