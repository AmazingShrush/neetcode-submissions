class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        res=float('inf')

        for i in range(n):
            res=min(nums[i],res)
        
        return res