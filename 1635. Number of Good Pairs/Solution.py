class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        meet = {}
        for i in range(len(nums)):
            if nums[i] in meet:
                meet[nums[i]] += 1
            else:
                meet[nums[i]] = 1
        
        for _, value in meet.items():
            result += value * (value - 1) // 2
        
        return result
