class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        opening = ['[','(','{']
        closing = [']','}',')']
        mapping = { ']':'[',')':'(','}':'{'}
        if s == '':
            return False
        for i in s:
            if i in opening:
                stk.append(i)
            if i in closing:
                if stk == [] or stk.pop() != mapping[i]:
                    return False
        
        if stk == []:
            return True
        
        return False
        