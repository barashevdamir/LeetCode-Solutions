class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def is_selfDividingNumber(num: int) -> bool:
            original = num
            while num > 0:
                digit = num % 10
                if digit == 0 or original % digit != 0:
                    return False
                num //= 10
            return True

        result = []
        for num in range(left, right + 1):
            if is_selfDividingNumber(num):
                result.append(num)

        return result