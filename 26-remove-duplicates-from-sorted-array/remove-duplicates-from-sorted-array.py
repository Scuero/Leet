class Solution(object):
    def removeDuplicates(self, nums):
        k = 1

        for indice in range(len(nums)):
            if nums[k-1] != nums[indice]:
                nums[k]=nums[indice]
                k += 1
        return k
        