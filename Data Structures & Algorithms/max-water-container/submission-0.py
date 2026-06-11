class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxAmount=0
        for i in range(0,n):
            for j in range(i+1,n):
                t = min(heights[i],heights[j])
                amt = t*abs(i-j)
                maxAmount = max(amt,maxAmount)
        return maxAmount