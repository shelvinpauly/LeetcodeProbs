class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        while len(nums) != 0:
            num = nums.pop()
            if num in nums:
                return True

        return False
