class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        balance = 0
        for digit in s:
            if digit == "L":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                answer += 1

        return answer
        