class Solution(object):
    def twoSum(self, nums, target):
        complementos = {}
        respuesta = []
        for indice, numero in enumerate(nums):
            complemento = target - numero
            if ( complemento in complementos ):
                respuesta.append(indice)
                respuesta.append(complementos[complemento])
            else:
                complementos[numero] = indice
        return respuesta