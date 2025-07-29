class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        seen = []

        for index, num in enumerate(nums):
            nums[index] += sum(seen)
            seen.append(num)

        return nums