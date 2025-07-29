class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 1:
            return nums[int(len(nums) / 2)]
        else:
            med1 = nums[int(len(nums) / 2) - 1]
            med2 = nums[int(len(nums) / 2)]
            return (med1 + med2) / 2.0