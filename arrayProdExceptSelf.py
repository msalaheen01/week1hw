class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        post= 1
        result = [0]*n
        for i in range(n):
            result[i] = pre
            pre *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= post
            post *= nums[i]
        return result