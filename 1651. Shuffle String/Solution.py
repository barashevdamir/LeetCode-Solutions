class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = s

        for i, ch in enumerate(s):
            index = indices[i]
            result = result[:index] + ch + result[index + 1:]

        return result 
        