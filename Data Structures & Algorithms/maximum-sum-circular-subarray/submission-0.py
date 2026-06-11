class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum=nums[0]
        minSum = nums[0]
        currMin=0
        currMax=0
        total = sum(nums)

        for n in nums:
            currMax = max(currMax,0) + n
            maxSum = max(currMax,maxSum)
            currMin = min(currMin,0)+n
            minSum = min(currMin,minSum)

        if maxSum > 0:
            return max(maxSum,total-minSum)
        else:
            return maxSum