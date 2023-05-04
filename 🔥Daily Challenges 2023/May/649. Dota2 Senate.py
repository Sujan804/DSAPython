from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        queue = deque()
        cntR, cntD, powR, powD = 0, 0, 0, 0

        for c in senate:
            queue.append(c)
            if c == 'R':
                cntR += 1
            else:
                cntD += 1
        queue.append('#')

        if cntR == 0 or cntD == 0:
            if cntR:
                return "Radiant"
            else:
                return "Dire"

        cntR = 0
        cntD = 0
        
        while 1:
            front = queue.popleft()
            if front == 'R':
                if powD>0:
                    powD -= 1
                else:
                    cntR += 1
                    powR += 1
                    queue.append(front)
            elif front == 'D':
                if powR>0:
                    powR -= 1
                else:
                    cntD += 1
                    powD += 1
                    queue.append(front)
            else:
                if cntR == 0:
                    return "Dire"
                if cntD == 0:
                    return "Radiant"
                cntR = 0
                cntD = 0
                queue.append('#')
            
            


        
