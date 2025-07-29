class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits_sum = 0
        digits_product = 1
        for digit in str(n):
            digits_sum += int(digit)
            digits_product *= int(digit)

        return digits_product - digits_sum