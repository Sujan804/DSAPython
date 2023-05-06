class DetectSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.pointsList = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.pointsList.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for (x, y) in self.pointsList:
            if abs(x-px) != abs(y-py) or px == x or py == y:
                continue
            res += self.pointsCount[(x,py)] * self.pointsCount[(px,y)]

        return res 

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)