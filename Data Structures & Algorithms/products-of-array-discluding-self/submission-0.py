class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        res=[]

        for i in range(0,n):
            prod = 1
            for j in range(n):
                if i==j:
                    continue
                prod = prod*nums[j]
            res.append(prod)
        return res