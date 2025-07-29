class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for index in range(len(s)):
            if stack and abs(ord(stack[-1]) - ord(s[index])) == 32:
                stack.pop()
            else:
                stack.append(s[index])
        
        return ''.join(stack)