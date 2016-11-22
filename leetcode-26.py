
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 1
        for n in nums:
            if n>nums[i-1]:
                nums[i]=n
                i+=1
        nums = nums[:i]
        return i