class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l,r = 0,n-1
        maxAmount=0
        nums = heights

        while l < r:
            t = min(nums[l],nums[r])
            amt = t*abs(l-r)

            if amt > maxAmount:
                maxAmount = amt
            
            if nums[l] <= nums[r]:
                l+=1
            else:
                r-=1
        return maxAmount