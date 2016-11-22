class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for x in nums[:]:
            if x==val:
                nums.remove(val)
        return len(nums)