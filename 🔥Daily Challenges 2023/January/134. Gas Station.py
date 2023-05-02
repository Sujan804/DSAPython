class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        totalFuel = 0
        totalCost = 0
        for i in range(len(gas)):
            totalFuel += gas[i]
            totalCost += cost[i]
        if(totalFuel < totalCost):
            return -1
        
        curFuel,start = 0,0
        for i in range(len(cost)):
            if curFuel < 0:
                start = i
                curFuel = 0
            curFuel += gas[i]-cost[i]
        
        return start
