class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet=set()
        L=0
        res=0
        for R in range(len(s)):
            while s[R] in subSet:
                subSet.remove(s[L])
                L+=1
            subSet.add(s[R])
            res = max(res, R-L+1)
        return res