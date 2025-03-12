class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefijo = ""
        for caracteres_en_tuplas in zip(*strs):
            if len( set(caracteres_en_tuplas) )==1:
                prefijo += (caracteres_en_tuplas[0])
            else:
                return prefijo
        return prefijo
        