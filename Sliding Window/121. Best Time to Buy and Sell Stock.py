class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        minArr = [0]*length
        maxArr = [0]*length
        curMin = prices[0]
       
        minArr[0] = curMin
        for i in range(1,length): 
            if prices[i]<curMin:
                curMin = prices[i]
            minArr[i] = curMin
        
        curMax = prices[length-1]

        maxArr[length-2] = curMax
        for i in range(length-1,-1,-1):
            if prices[i] > curMax:
                curMax = prices[i]
            maxArr[i] = curMax

        maxProfit = 0
        for i in range(0, length):
            if maxProfit < (maxArr[i]-minArr[i]):
                maxProfit = maxArr[i]- minArr[i]

        return maxProfit


#Blind75