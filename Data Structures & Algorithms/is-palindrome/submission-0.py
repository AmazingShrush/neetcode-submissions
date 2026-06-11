class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','')
        res=''
        for c in s:
            if c.isalnum():
                res+=c.lower()
        L=0
        R=len(res)-1

        while L<R:
            if res[L] == res[R]:
                L+=1
                R-=1
            else:
                return False
        return True
        

