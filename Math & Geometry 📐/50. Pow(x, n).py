class Solution:
    def myPow(self, x: float, n: int) -> float:

        def funct(base = x, exponent = abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return funct(base*base, exponent//2)
            else:
                return base*funct(base*base,  exponent//2)
        f = funct()

        return float(f) if n>=0 else 1/f

        