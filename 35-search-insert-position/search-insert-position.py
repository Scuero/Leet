class Solution(object):
    def searchInsert(self, nums, target):
        inicio = 0
        fin = len(nums)-1
        encontrado = False
        while inicio <= fin:
            medio = int( (fin+inicio)/2 )
            if nums[medio] == target:
                return medio
            if nums[medio] < target:
                inicio = medio+1
            else:
                fin = medio-1
        return inicio