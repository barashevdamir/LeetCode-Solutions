class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for ind, val in enumerate(nums):
            result.insert(index[ind], val)
        return result