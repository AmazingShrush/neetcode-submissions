class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors=0

        for i in range(len(details)):
            age_str = details[i][-4:-2]
            age = int(age_str)

            if age > 60:
                seniors+=1
        return seniors