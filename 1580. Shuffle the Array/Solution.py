class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n
        result = []
        for _ in range(n):
            result.append(nums[left])
            result.append(nums[right])
            left += 1
            right += 1
        
        return result
