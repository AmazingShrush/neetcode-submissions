class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        length=1
        for i in range(len(s)):
            currSubstring = {s[i]}
            for j in range(i+1,len(s)):
                if s[j] not in currSubstring:
                    currSubstring.add(s[j])
                    length = max(length,len(currSubstring))
                else:
                    break
        return length