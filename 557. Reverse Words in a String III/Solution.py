class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        result = []

        for word in words:
            result.append(''.join(reversed(word))) 
        
        return ' '.join(result)
        

        