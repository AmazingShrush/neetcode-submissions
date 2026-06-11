class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i in range(0,len(nums)):
            # if seen == {} and i==0:
            #     seen[nums[i]]=i
            val= target-nums[i] 
            if val in seen:
                return [seen[val],i]
            else:
                seen[nums[i]]=i
        return []