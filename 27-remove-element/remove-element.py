class Solution(object):
    def removeElement(self, nums, val):
        contador = 0
        while val in nums:
            nums.remove(val)
            contador += 1
        print(nums)
        print(contador)
        