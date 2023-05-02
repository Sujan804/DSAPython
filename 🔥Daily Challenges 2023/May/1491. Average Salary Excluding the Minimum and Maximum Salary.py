class Solution:
    def average(self, salary: List[int]) -> float:
        Min, Max = salary[0], salary[0]
        Sum = 0
        for s in salary:
            Sum += s
            if s<Min:
                Min = s
            if s>Max:
                Max = s
        
        Sum -= (Min+Max)

        l = len(salary) - 2

        return Sum/l