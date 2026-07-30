class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = 1
        max_prod = float("-inf")

        for num in nums:
            prod *= num
            max_prod = max(max_prod, prod)
            if prod == 0:
                prod = 1

        nums.reverse()

        prod = 1

        for num in nums:
            prod *= num
            max_prod = max(max_prod, prod)
            if prod == 0:
                prod = 1

        return max_prod 