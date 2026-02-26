#week01-5
#238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preSum = [1]
        postSum = [1]
        for i in range(n - 1):
            preSum.append(preSum[-1] * nums[i])
            postSum.append(postSum[-1] * nums[n - 1 - i])
        ans = []
        for i in range(n):
            ans.append(preSum[i] * postSum[n-1-i])
        return ans