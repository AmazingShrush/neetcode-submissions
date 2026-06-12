class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk=[]
        res=0
        operands = ['+','-','*','/']
        for i in range(len(tokens)):
            if tokens[i] == '+' and len(stk)>=2:
                if stk[-1] and stk[-2] not in operands:

                    t=int(stk[-2]) + int(stk[-1])
                    stk.pop()
                    stk.pop()
                    stk.append(t)
            elif tokens[i] == '-' and len(stk)>=2:
                if stk[-1] and stk[-2] not in operands:
                    t=int(stk[-2]) - int(stk[-1])
                    stk.pop()
                    stk.pop()
                    stk.append(t)
            elif tokens[i] == '*' and len(stk)>=2:
                if stk[-1] and stk[-2] not in operands:
                    t=int(stk[-2]) * int(stk[-1])
                    stk.pop()
                    stk.pop()
                    stk.append(t)
            elif tokens[i] == '/' and len(stk)>=2:
                if stk[-1] and stk[-2] not in operands and stk[-1] !=0:
                    t=int(stk[-2]) / int(stk[-1])
                    stk.pop()
                    stk.pop()
                    stk.append(t)
            else:
                stk.append(tokens[i])
            
        if stk:
            res=stk[0]
        return int(res)