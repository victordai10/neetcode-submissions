class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # trailing products
        n = len(nums)
        left = [1] * n
        right = [1] * n

        # left pass:
        prod = 1
        for i in range(n):
            if i > 0:
                prod *= nums[i - 1]
            left[i] = prod
        # right pass
        prod = 1
        for j in range(n - 1, -1, -1):
            if j < n - 1:
                prod *= nums[j + 1]
            right[j] = prod
        
        res = [1] * n
        for k in range(n):
            res[k] = left[k] * right[k]
        return res