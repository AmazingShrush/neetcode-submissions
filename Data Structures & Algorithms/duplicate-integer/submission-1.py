class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        seen={}
        for i in range(0,n):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = i
        return False