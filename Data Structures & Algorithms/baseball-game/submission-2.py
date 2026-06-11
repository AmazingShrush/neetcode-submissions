class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        sum=0
        for i in range(0,len(operations)):
            if operations[i] == '+':
                res.append(int(res[-1])+int(res[-2]))
            elif operations[i] == 'C':
                res.pop()
            elif operations[i] == 'D':
                res.append(2*int(res[-1]))
            else:
                res.append(int(operations[i]))

        
        for i in res:
            sum+=i
        return sum