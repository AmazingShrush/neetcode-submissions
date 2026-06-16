class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi = None
        arr=[]

        if k==1:
            return nums

        for i in range(0,len(nums)-k+1):
            window = nums[i:i+k]
            maxi = window[0]
            for j in range(0,len(window)):
                if window[j]>maxi:
                    maxi = window[j]
            arr.append(maxi)

        return arr