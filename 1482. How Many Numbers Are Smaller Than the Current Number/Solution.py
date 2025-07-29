class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        for num in nums:
            less = 0
            for key, value in seen.items():
                if key < num:
                    less += value

            result.append(less)

        return result
